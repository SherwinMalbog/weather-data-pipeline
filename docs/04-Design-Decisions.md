# Design Decisions

Written as short ADRs (Architecture Decision Records) — the format real engineering teams use to document *why*, not just *what*. Learn this format; being able to produce one in an interview is itself a signal of engineering maturity.

---

### ADR-01: ELT instead of ETL

**Decision:** Load raw data into the warehouse first, transform afterward with dbt.

**Why:** Raw data is never thrown away or mutated before storage. If a transformation has a bug, we fix the dbt model and re-run — we don't need to re-extract from the API. This also matches how most modern data teams actually work.

**Trade-off:** Slightly more storage used (raw JSON + structured tables), which is irrelevant at this scale.

---

### ADR-02: MinIO instead of a real cloud bucket

**Decision:** Use MinIO, an open-source S3-compatible object store, run locally in Docker.

**Why:** Same API as S3 (`boto3` doesn't know the difference). No account, no credit card, no risk of a surprise bill. Code written against MinIO works against real S3 by changing only the endpoint URL and credentials.

---

### ADR-03: PostgreSQL instead of a cloud warehouse

**Decision:** Use PostgreSQL as the warehouse.

**Why:** Free, runs anywhere, and dbt treats it as a first-class warehouse. The SQL and dbt models you write are portable to Redshift, Snowflake, or BigQuery with minor syntax differences.

---

### ADR-04: dbt for transformations, not raw Python/SQL scripts

**Decision:** All transformation logic lives in dbt models, not ad-hoc scripts.

**Why:** dbt gives version-controlled SQL, automatic dependency ordering, built-in testing, and auto-generated documentation — all things a hand-rolled script would need to build from scratch. It's also one of the most commonly requested skills in current data engineer/analyst postings.

---

### ADR-05: Airflow with LocalExecutor, not CeleryExecutor

**Decision:** Run Airflow in `standalone` mode with a single executor, not a distributed Celery/Redis worker setup.

**Why:** This project runs 5 small tasks once a day. A distributed task queue would be solving a scaling problem this project doesn't have. Know the difference and be ready to explain when you *would* reach for CeleryExecutor/KubernetesExecutor (high task volume, need to scale workers horizontally).

---

### ADR-06: Open-Meteo as the data source

**Decision:** Use the Open-Meteo weather API.

**Why:** No API key, no signup, no rate-limit headaches, and it returns genuinely time-varying data — the pipeline is doing real, non-fake incremental work every time it runs, which is what makes this different from a "toy" project built on a static CSV.

---

### ADR-07: Metabase instead of Power BI/Tableau

**Decision:** Use Metabase for the BI layer.

**Why:** Free, open-source, runs in one Docker container, connects to Postgres with zero configuration. The visualization concepts (build a question, save a dashboard) transfer directly to Power BI or Looker Studio.

---

## How to use this file

When you make a real change to the project (swap a tool, change a schema, add a layer), add a new ADR here. This file *is* your engineering judgment on display — treat it like a work sample, because in an interview, it is one.
