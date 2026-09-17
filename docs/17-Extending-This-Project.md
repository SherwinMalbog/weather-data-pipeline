# Extending This Project

Do these *after* the base project works end-to-end — don't let this list stop you from finishing the core version first.

## Easy additions (a weekend each)
- Add a second data source (e.g. a free currency exchange API) and join it against weather data in a new mart
- Add a Slack/email alert on Airflow task failure
- Add an `accepted_values` or custom SQL test in dbt

## Medium additions
- Swap Metabase for a Streamlit dashboard you build yourself (more Python, more control)
- Add a dbt intermediate layer as the project grows past two layers
- Add data lineage documentation via `dbt docs`

## Bigger additions (genuinely different skill, don't rush this)
- Point the same code at a real free-tier cloud warehouse (BigQuery's free tier is the easiest on-ramp — verify current terms before relying on it)
- Add a streaming component (Kafka) for a second, real-time version of this pipeline alongside the batch one
- Add Great Expectations for more expressive data quality checks than dbt tests alone

## A note on scope creep

Every one of these is optional. A finished, well-documented, correctly-scoped small project beats an ambitious half-finished one in every interview. Ship the base version first.
