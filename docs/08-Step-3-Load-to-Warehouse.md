# Step 3 — Load to the Warehouse

## Goal

Read today's raw files out of MinIO and insert structured rows into a staging table in Postgres.

## File

`src/load/load_to_warehouse.py`

## Table created

`raw.weather_readings` — one row per API call, per city, per fetch time. Includes both the parsed fields (`temperature`, `windspeed`, ...) **and** the full original JSON in a `JSONB` column (`raw_payload`), so nothing is lost even if the parsed columns miss something you need later.

## Idempotency

The `source_file` column is unique, and inserts use `ON CONFLICT (source_file) DO NOTHING`. Running the load step twice on the same files won't create duplicates. This matters because Airflow *will* retry failed tasks — your load step needs to be safe to re-run.

## Run it standalone to test

```bash
docker compose up -d postgres
export WAREHOUSE_HOST=localhost
python3 -m src.load.load_to_warehouse
```

## Verify

```bash
docker exec -it weather_postgres psql -U warehouse -d warehouse -c "select city, fetched_at, temperature from raw.weather_readings order by fetched_at desc limit 10;"
```

Next: [[09-Step-4-Transform-with-dbt]]
