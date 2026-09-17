# How to Talk About This on Your Resume

## Resume bullet options (pick 2–3, don't use all of them — that reads as padding)

- Built an end-to-end ELT pipeline (Python, Airflow, dbt, PostgreSQL) that ingests API data daily into a data-lake-and-warehouse architecture
- Designed a staging-to-marts dbt data model with automated data quality tests (uniqueness, null checks)
- Containerized a 5-service data platform (object storage, warehouse, orchestrator, BI tool) with Docker Compose
- Set up a CI pipeline (GitHub Actions) to automatically lint and test pipeline code on every commit
- Documented system architecture and design decisions (ADRs) for a personal data engineering project

## Why this works for more than "Data Engineer" postings

| Role | What to emphasize from this project |
|---|---|
| Data Engineer | the full pipeline: extract, load, orchestration, dbt models |
| Data Analyst | the dbt marts, the SQL, the Metabase dashboard |
| BI Analyst | the Metabase dashboard, the data modeling behind it |
| ETL Developer | the extract/load Python scripts, idempotency handling |
| Junior Cloud Data Engineer | [[03-Cloud-Service-Equivalents]] — lead with "built against Postgres/MinIO using the same ELT pattern used against Redshift/S3 or BigQuery/Cloud Storage" |

## Likely interview questions this project prepares you for

- "Walk me through a project you built." → walk the architecture diagram in [[02-Architecture]]
- "Why did you choose X over Y?" → answer straight from [[04-Design-Decisions]]
- "How do you make sure your data is correct?" → talk about [[11-Step-6-Data-Quality-Tests]]
- "Have you worked with orchestration tools?" → yes, Airflow, with retries and scheduling — [[10-Step-5-Orchestrate-with-Airflow]]
- "What would you do differently at scale?" → say it honestly: swap LocalExecutor for CeleryExecutor/KubernetesExecutor, swap Postgres for a columnar warehouse, add partitioning — see [[17-Extending-This-Project]]

## Be honest about scope

Don't claim "production experience" or "petabyte-scale" — you didn't do that. Describe this accurately as a self-directed project. Interviewers respect accurate scoping far more than inflated claims that fall apart under one follow-up question.

Next: [[17-Extending-This-Project]]
