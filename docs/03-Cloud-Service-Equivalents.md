# Cloud Service Equivalents

The whole point of this project is that it **behaves like a real cloud data platform** without needing an AWS/Azure/GCP account or a credit card. Every local tool below is a stand-in for a specific managed cloud service — same concepts, same architecture pattern, different price tag ($0).

| What it does | This project uses | AWS equivalent | Azure equivalent | GCP equivalent |
|---|---|---|---|---|
| Object storage / data lake | MinIO | S3 | Blob Storage / ADLS Gen2 | Cloud Storage |
| Relational data warehouse | PostgreSQL | Redshift / RDS | Azure SQL / Synapse | BigQuery / Cloud SQL |
| Workflow orchestration | Airflow | MWAA (Managed Airflow) | Data Factory | Cloud Composer |
| Data transformation | dbt | dbt (same tool — runs on top of any warehouse) | dbt | dbt |
| Containers / compute | Docker Compose | ECS / Fargate | Container Apps / ACI | Cloud Run |
| CI/CD | GitHub Actions | CodePipeline / CodeBuild | Azure DevOps Pipelines | Cloud Build |
| BI / dashboards | Metabase | QuickSight | Power BI | Looker Studio |

## Why this matters for interviews

When an interviewer asks "have you worked with cloud data warehouses?" you can honestly say: *"I built a pipeline against Postgres using the same ELT pattern — extract to a data lake, load to a warehouse, transform with dbt — that I'd use against Redshift, Synapse, or BigQuery. The SQL and the dbt models don't really change; only the connection details do."* That's true, and it's a defensible answer.

## What genuinely does NOT transfer

Be honest about this in interviews:
- Cloud IAM/security configuration (roles, policies, VPCs) — you haven't touched this
- Cost management and cloud billing behavior
- Cloud-specific scaling/performance behavior (e.g. Redshift distribution keys, BigQuery partitioning/clustering) — the concepts are similar but you haven't hit real-world scale
- Managed-service operational quirks (e.g. how MWAA differs from open-source Airflow)

If asked directly, say so — then pivot to what you *can* speak to concretely: the pipeline pattern, the SQL, the dbt models, the orchestration logic.

## If you later get free-tier cloud access

Every layer here has a real free-tier path if you want to go further later (see [[17-Extending-This-Project]]):
- AWS: S3 + Redshift Serverless free trial, or S3 + Athena (pay-per-query, pennies)
- Azure: Blob Storage + free-tier Azure SQL Database
- GCP: Cloud Storage + BigQuery (perpetually free tier for queries, subject to current terms)

None of these are required to finish this project.
