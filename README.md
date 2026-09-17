# Weather Data Pipeline — Local Cloud-Emulation Portfolio Project

An end-to-end ELT data pipeline that ingests free public weather data through a data lake, a warehouse, dbt transformations, Airflow orchestration, and a BI dashboard — all running locally, for free, with no cloud account required.

**Architecture emulates AWS / Azure / GCP equivalents.** See `docs/03-Cloud-Service-Equivalents.md`.

## Stack

Python · PostgreSQL · MinIO (S3-compatible) · Apache Airflow · dbt · Docker Compose · Metabase · GitHub Actions

## Quick start

```bash
cp .env.example .env
cp dbt_project/profiles.yml.example dbt_project/profiles.yml
docker compose up -d --build
```

Then open:
- Airflow: http://localhost:8080 (get the auto-generated password with `docker compose logs airflow | grep -i password`)
- MinIO console: http://localhost:9001 (login: minioadmin / minioadmin)
- Metabase: http://localhost:3000

Full walkthrough: open the `docs/` folder in Obsidian (or just read the files in order starting with `docs/00-Start-Here.md`).

## Project structure

```
.
├── docs/               # step-by-step build guide (Obsidian vault)
├── config/             # cities.yaml — what data to pull
├── src/                # extract + load Python code
├── dags/               # Airflow DAG
├── dbt_project/        # dbt models, tests, seeds
├── sql/                # warehouse bootstrap SQL
├── tests/              # unit tests
├── .github/workflows/  # CI pipeline
└── docker-compose.yml
```

## Why this project exists

Built to close the gap between "completed data engineering courses/certifications" and "have built something end-to-end." Full reasoning in `docs/04-Design-Decisions.md`.

## License

MIT — use this as a template for your own portfolio project.
