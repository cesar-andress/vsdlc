"""GitHub REST API client with retry and rate-limit handling."""

from __future__ import annotations

import logging
import os
import time
from typing import Any

import httpx

from vsdlc_mining.config import (
    DEFAULT_PER_PAGE,
    GITHUB_API_BASE,
    INITIAL_BACKOFF_SECONDS,
    MAX_CODE_SEARCH_PAGES,
    MAX_REPO_SEARCH_PAGES,
    MAX_RETRIES,
    CORE_RATE_LIMIT_BUFFER,
    CORE_REQUEST_MIN_INTERVAL_SECONDS,
    MAX_PRIMARY_RATE_LIMIT_SLEEP_SECONDS,
    RATE_LIMIT_WAIT_CHUNK_SECONDS,
    SEARCH_PAGE_DELAY_SECONDS,
    SEARCH_RATE_LIMIT_BUFFER,
    SECONDARY_RATE_LIMIT_MAX_SECONDS,
)

logger = logging.getLogger(__name__)


class GitHubClientError(RuntimeError):
    """Raised when GitHub API calls fail after retries."""


class GitHubRateLimitExceeded(GitHubClientError):
    """Raised when waiting for quota reset would block longer than configured."""

    def __init__(
        self,
        message: str,
        *,
        resource: str,
        sleep_seconds: float,
        reset_at: str | None = None,
    ) -> None:
        super().__init__(message)
        self.resource = resource
        self.sleep_seconds = sleep_seconds
        self.reset_at = reset_at


def _error_message(response: httpx.Response) -> str:
    try:
        payload = response.json()
    except ValueError:
        return response.text
    if isinstance(payload, dict):
        return str(payload.get("message", ""))
    return response.text


def _is_rate_limited(response: httpx.Response) -> bool:
    if response.status_code not in {403, 429}:
        return False
    message = _error_message(response).lower()
    if "rate limit" in message or "secondary rate" in message:
        return True
    remaining = response.headers.get("X-RateLimit-Remaining")
    if remaining is not None and remaining.isdigit() and int(remaining) == 0:
        return True
    return response.status_code == 429


def _is_secondary_rate_limited(response: httpx.Response) -> bool:
    return "secondary rate" in _error_message(response).lower()


def _format_reset_time(reset_header: str | None) -> str | None:
    if not reset_header:
        return None
    try:
        reset_at = float(reset_header)
    except ValueError:
        return None
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(reset_at))


def _sleep_waiting(
    client: GitHubClient,
    delay: float,
    *,
    headline: str,
    reset_label: str | None = None,
) -> None:
    """Sleep until quota reset in short chunks with periodic status logs."""
    if delay <= RATE_LIMIT_WAIT_CHUNK_SECONDS:
        time.sleep(delay)
        return

    logger.warning(
        "%s Waiting %.0fs total%s.",
        headline,
        delay,
        f"; quota resets ~{reset_label}" if reset_label else "",
    )
    remaining = delay
    deadline = time.time() + delay
    while remaining > 0:
        chunk = min(RATE_LIMIT_WAIT_CHUNK_SECONDS, remaining)
        eta = time.strftime("%H:%M:%S", time.localtime(deadline))
        logger.info(
            "%s Pausing %.0fs (~%.0fs left, resume around %s).",
            headline,
            chunk,
            remaining,
            eta,
        )
        time.sleep(chunk)
        remaining -= chunk
        if remaining <= 0:
            return
        try:
            payload = client.get_rate_limit()
            core = payload.get("resources", {}).get("core", {})
            quota_remaining = int(core.get("remaining", 0))
            if quota_remaining > 0:
                logger.info(
                    "%s Core quota available again (%d/%s). Resuming early.",
                    headline,
                    quota_remaining,
                    core.get("limit", "?"),
                )
                return
        except GitHubClientError:
            logger.debug("Rate-limit status check failed; continuing wait.", exc_info=True)


class GitHubClient:
    """Thin wrapper around GitHub REST v3 with audit-friendly logging."""

    def __init__(
        self,
        token: str | None = None,
        timeout: float = 30.0,
        per_page: int = DEFAULT_PER_PAGE,
        *,
        wait_for_rate_limit: bool = True,
    ) -> None:
        self.token = token or os.environ.get("GITHUB_TOKEN")
        if not self.token:
            raise GitHubClientError(
                "GITHUB_TOKEN environment variable is required for API access."
            )
        self.per_page = per_page
        self.wait_for_rate_limit = wait_for_rate_limit
        self._last_core_request_at = 0.0
        self._client = httpx.Client(
            base_url=GITHUB_API_BASE,
            timeout=timeout,
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {self.token}",
                "X-GitHub-Api-Version": "2022-11-28",
            },
        )

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> GitHubClient:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()

    def _sleep_for_rate_limit(self, response: httpx.Response, attempt: int) -> None:
        resource = response.headers.get("X-RateLimit-Resource", "unknown")
        reset = response.headers.get("X-RateLimit-Reset")
        reset_label = _format_reset_time(reset)
        retry_after = response.headers.get("Retry-After")

        if _is_secondary_rate_limited(response):
            if retry_after:
                delay = min(float(retry_after), SECONDARY_RATE_LIMIT_MAX_SECONDS)
            else:
                delay = min(
                    INITIAL_BACKOFF_SECONDS * (2**attempt),
                    SECONDARY_RATE_LIMIT_MAX_SECONDS,
                )
            logger.warning(
                "Secondary rate limit (%s, resource=%s). Sleeping %.1fs before retry.",
                response.status_code,
                resource,
                delay,
            )
            time.sleep(delay)
            return

        if retry_after:
            delay = float(retry_after)
        else:
            delay = INITIAL_BACKOFF_SECONDS * (2**attempt)
        if reset:
            reset_delay = max(0.0, float(reset) - time.time() + 1.0)
            delay = max(delay, reset_delay)
        if (
            not self.wait_for_rate_limit
            and delay > MAX_PRIMARY_RATE_LIMIT_SLEEP_SECONDS
        ):
            message = (
                f"Core API quota exhausted ({resource}). "
                f"Would sleep {delay:.1f}s"
            )
            if reset_label:
                message += f"; resume after ~{reset_label}"
            raise GitHubRateLimitExceeded(
                message,
                resource=resource,
                sleep_seconds=delay,
                reset_at=reset_label,
            )
        if reset_label:
            logger.warning(
                "Rate limited (%s, resource=%s). Sleeping %.1fs; quota resets ~%s.",
                response.status_code,
                resource,
                delay,
                reset_label,
            )
        else:
            logger.warning(
                "Rate limited (%s, resource=%s). Sleeping %.1fs before retry.",
                response.status_code,
                resource,
                delay,
            )
        headline = f"Rate limited ({response.status_code}, resource={resource})"
        _sleep_waiting(
            self,
            delay,
            headline=headline,
            reset_label=reset_label,
        )

    def get_rate_limit(self) -> dict[str, Any]:
        """Read current quota without pacing side effects."""
        response = self._client.get("/rate_limit")
        if response.is_error:
            raise GitHubClientError(
                f"GitHub API error {response.status_code} for GET /rate_limit: "
                f"{_error_message(response)[:500]}"
            )
        payload = response.json()
        if not isinstance(payload, dict):
            raise GitHubClientError("Expected JSON object from GET /rate_limit")
        return payload

    def _throttle_core_request(self, path: str) -> None:
        """Pace core REST calls to stay under the hourly quota."""
        if path.startswith("/search"):
            return
        elapsed = time.time() - self._last_core_request_at
        if elapsed < CORE_REQUEST_MIN_INTERVAL_SECONDS:
            time.sleep(CORE_REQUEST_MIN_INTERVAL_SECONDS - elapsed)

    def _maybe_throttle_core(self, response: httpx.Response, path: str) -> None:
        """Pause proactively when core quota is nearly exhausted."""
        if path.startswith("/search"):
            return
        resource = response.headers.get("X-RateLimit-Resource", "")
        remaining = response.headers.get("X-RateLimit-Remaining")
        reset = response.headers.get("X-RateLimit-Reset")
        if resource not in {"", "core"} or remaining is None or not remaining.isdigit():
            return
        remaining_count = int(remaining)
        if remaining_count >= CORE_RATE_LIMIT_BUFFER:
            return
        if remaining_count == 0:
            reset_label = _format_reset_time(reset)
            reset_delay = max(0.0, float(reset) - time.time() + 1.0) if reset else 0.0
            if (
                not self.wait_for_rate_limit
                and reset_delay > MAX_PRIMARY_RATE_LIMIT_SLEEP_SECONDS
            ):
                message = f"Core API quota exhausted ({remaining_count} remaining)."
                if reset_label:
                    message += f" Resume after ~{reset_label}."
                raise GitHubRateLimitExceeded(
                    message,
                    resource=resource or "core",
                    sleep_seconds=reset_delay,
                    reset_at=reset_label,
                )
            logger.warning(
                "Core API quota exhausted (%d remaining). Sleeping %.1fs until reset ~%s.",
                remaining_count,
                reset_delay,
                reset_label or "unknown",
            )
            _sleep_waiting(
                self,
                reset_delay,
                headline="Core API quota exhausted",
                reset_label=reset_label,
            )
            return
        delay = CORE_REQUEST_MIN_INTERVAL_SECONDS * max(
            1,
            CORE_RATE_LIMIT_BUFFER - remaining_count,
        )
        delay = min(delay, 30.0)
        logger.info(
            "Core quota low (%d remaining). Slowing down %.1fs before next request.",
            remaining_count,
            delay,
        )
        time.sleep(delay)

    def _maybe_throttle_search(self, response: httpx.Response) -> None:
        """Pause proactively when search quota is nearly exhausted."""
        resource = response.headers.get("X-RateLimit-Resource", "")
        remaining = response.headers.get("X-RateLimit-Remaining")
        reset = response.headers.get("X-RateLimit-Reset")
        if resource != "search" or remaining is None or not remaining.isdigit():
            return
        remaining_count = int(remaining)
        if remaining_count >= SEARCH_RATE_LIMIT_BUFFER:
            return
        delay = SEARCH_PAGE_DELAY_SECONDS
        if reset:
            delay = max(delay, max(0.0, float(reset) - time.time() + 1.0))
        logger.info(
            "Search quota low (%d remaining). Sleeping %.1fs.",
            remaining_count,
            delay,
        )
        time.sleep(delay)

    def request(self, method: str, path: str, **kwargs: Any) -> httpx.Response:
        """Issue an HTTP request with exponential backoff on transient errors."""
        last_error: Exception | None = None
        for attempt in range(MAX_RETRIES):
            if method.upper() == "GET":
                self._throttle_core_request(path)
            try:
                response = self._client.request(method, path, **kwargs)
            except httpx.HTTPError as exc:
                last_error = exc
                delay = INITIAL_BACKOFF_SECONDS * (2**attempt)
                logger.warning("HTTP error on %s %s: %s; retry in %.1fs", method, path, exc, delay)
                time.sleep(delay)
                continue

            if method.upper() == "GET" and not path.startswith("/search"):
                self._last_core_request_at = time.time()

            if _is_rate_limited(response):
                self._sleep_for_rate_limit(response, attempt)
                continue

            if response.is_error:
                raise GitHubClientError(
                    f"GitHub API error {response.status_code} for {method} {path}: "
                    f"{_error_message(response)[:500]}"
                )

            if path == "/search/code":
                self._maybe_throttle_search(response)
            elif path == "/search/repositories":
                self._maybe_throttle_search(response)
            else:
                self._maybe_throttle_core(response, path)
            return response

        if last_error:
            raise GitHubClientError(
                f"GitHub request failed after retries: {last_error}"
            ) from last_error
        raise GitHubClientError(f"GitHub request failed after retries: {method} {path}")

    def get_json(self, path: str, params: dict[str, Any] | None = None) -> Any:
        response = self.request("GET", path, params=params)
        return response.json()

    def paginate(
        self,
        path: str,
        params: dict[str, Any] | None = None,
        *,
        max_items: int | None = None,
    ) -> list[Any]:
        """Follow GitHub pagination until exhaustion or max_items."""
        page_params = dict(params or {})
        page_params.setdefault("per_page", self.per_page)
        items: list[Any] = []
        page = 1
        while True:
            page_params["page"] = page
            batch = self.get_json(path, params=page_params)
            if not isinstance(batch, list):
                raise GitHubClientError(f"Expected list response from {path}, got {type(batch)}")
            if not batch:
                break
            items.extend(batch)
            if max_items is not None and len(items) >= max_items:
                return items[:max_items]
            if len(batch) < page_params["per_page"]:
                break
            page += 1
        return items

    def search_repositories(
        self,
        query: str,
        *,
        max_results: int,
        max_pages: int | None = None,
    ) -> list[dict[str, Any]]:
        """Run GitHub repository search with pagination capped at max_results."""
        page_cap = max_pages if max_pages is not None else MAX_REPO_SEARCH_PAGES
        results: list[dict[str, Any]] = []
        page = 1
        while len(results) < max_results and page <= page_cap:
            if page > 1:
                time.sleep(SEARCH_PAGE_DELAY_SECONDS)
            try:
                payload = self.get_json(
                    "/search/repositories",
                    params={"q": query, "per_page": self.per_page, "page": page},
                )
            except GitHubClientError as exc:
                if "Only the first 1000" in str(exc):
                    logger.info(
                        "Repository search hit GitHub 1000-result cap for query %r at page %d.",
                        query,
                        page,
                    )
                    break
                raise

            items = payload.get("items", [])
            total_count = int(payload.get("total_count") or 0)
            if not items:
                break
            results.extend(items)
            logger.debug(
                "Repository search page %d for %r: %d items (total_count=%d, collected=%d).",
                page,
                query,
                len(items),
                total_count,
                len(results),
            )
            if len(items) < self.per_page:
                break
            if len(results) >= max_results:
                break
            if page >= page_cap:
                logger.info(
                    "Stopping repository search for %r at page %d (max_pages=%d).",
                    query,
                    page,
                    page_cap,
                )
                break
            page += 1
        return results[:max_results]

    def search_code(
        self,
        query: str,
        *,
        max_results: int,
        max_pages: int | None = None,
    ) -> list[dict[str, Any]]:
        """Run GitHub code search with pagination capped at max_results."""
        page_cap = max_pages if max_pages is not None else MAX_CODE_SEARCH_PAGES
        results: list[dict[str, Any]] = []
        page = 1
        while len(results) < max_results and page <= page_cap:
            if page > 1:
                time.sleep(SEARCH_PAGE_DELAY_SECONDS)
            try:
                payload = self.get_json(
                    "/search/code",
                    params={"q": query, "per_page": self.per_page, "page": page},
                )
            except GitHubClientError as exc:
                if "Only the first 1000" in str(exc):
                    logger.info(
                        "Code search hit GitHub 1000-result cap for query %r at page %d.",
                        query,
                        page,
                    )
                    break
                raise

            items = payload.get("items", [])
            total_count = int(payload.get("total_count") or 0)
            if not items:
                break
            results.extend(items)
            logger.debug(
                "Code search page %d for %r: %d items (total_count=%d, collected=%d).",
                page,
                query,
                len(items),
                total_count,
                len(results),
            )
            if len(items) < self.per_page:
                break
            if len(results) >= max_results:
                break
            if page >= page_cap:
                logger.info(
                    "Stopping code search for %r at page %d (max_pages=%d).",
                    query,
                    page,
                    page_cap,
                )
                break
            page += 1
        return results[:max_results]

    def get_repository(self, full_name: str) -> dict[str, Any]:
        owner, repo = full_name.split("/", 1)
        return self.get_json(f"/repos/{owner}/{repo}")

    def list_repo_root_entries(self, full_name: str) -> list[dict[str, Any]]:
        owner, repo = full_name.split("/", 1)
        try:
            return self.get_json(f"/repos/{owner}/{repo}/contents/")
        except GitHubClientError as exc:
            if "404" in str(exc):
                return []
            raise

    def path_exists(self, full_name: str, path: str) -> bool:
        owner, repo = full_name.split("/", 1)
        try:
            self.get_json(f"/repos/{owner}/{repo}/contents/{path}")
            return True
        except GitHubClientError as exc:
            if "404" in str(exc):
                return False
            raise

    def list_tags(self, full_name: str, *, limit: int = 5) -> list[dict[str, Any]]:
        owner, repo = full_name.split("/", 1)
        return self.paginate(f"/repos/{owner}/{repo}/tags", max_items=limit)

    def list_releases(self, full_name: str, *, limit: int = 5) -> list[dict[str, Any]]:
        owner, repo = full_name.split("/", 1)
        return self.paginate(f"/repos/{owner}/{repo}/releases", max_items=limit)
