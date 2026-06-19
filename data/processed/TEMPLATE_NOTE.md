# Annotation templates (not results)

Files named `*_template.jsonl` and `*_template.csv` in this directory are **empty annotation scaffolds** (schema v0.2).

- Do **not** treat them as empirical outputs.
- Primary field: `primary_label` (`AI_PRODUCT` | `CONVENTIONAL_SOFTWARE` | `EXCLUDE`).
- Optional: `secondary_tags` (pipe-separated).
- Deprecated: v0.1 `label` column (`TOOL`/`ASSIST`/`MIXED`/`UNCLEAR`) — not for primary analysis.
- See `docs/annotation_protocol.md` and `docs/annotation_example.json`.
- Schema: `~/papers/vsdlc/docs/classification_schema.md`
