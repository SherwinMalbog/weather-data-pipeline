# Step 5 — Orchestrate with Airflow

## Goal

Chain extract → load → dbt seed → dbt run → dbt test into one DAG that runs on a schedule and retries on failure.

## File

`dags/weather_pipeline_dag.py`

## Why not just a cron job?

A cron job can run a script on a schedule too — but it can't easily:
- retry a single failed step without re-running everything before it
- show you *which* step failed and why, in a UI
- express "step B depends on step A finishing successfully" as a first-class concept
- backfill a missed run for a specific past date

That's what Airflow (or any orchestrator — Prefect, Dagster, cloud-native equivalents) is for.

## Start Airflow

```bash
docker compose up -d
```

Check the logs for the auto-generated admin password:

```bash
docker compose logs airflow | grep -i password
```

Open http://localhost:8080, log in, and find the `weather_pipeline` DAG.

## Trigger it manually

Click the ▶ button in the Airflow UI, or:

```bash
docker exec -it weather_airflow airflow dags trigger weather_pipeline
```

## Read the DAG code

Notice the task dependency line at the bottom:

```python
extract >> load >> dbt_seed >> dbt_run >> dbt_test
```

This one line *is* the pipeline. Everything else just defines what each step does.

Next: [[11-Step-6-Data-Quality-Tests]]
