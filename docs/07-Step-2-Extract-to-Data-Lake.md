# Step 2 — Extract to the Data Lake

## Goal

Call the API for every configured city and store the **raw, untouched** response in MinIO — this is your data lake's "raw zone" or "bronze layer."

## File

`src/extract/fetch_weather.py`

## Key idea: never transform in the extract step

The extract script does not calculate anything, rename fields, or drop data. It wraps the raw API response with a bit of metadata (`city`, `fetched_at`) and writes it out as-is. See [[04-Design-Decisions]] (ADR-01) for why.

## Storage layout in MinIO

```
raw-weather/
  raw/
    Manila/
      2026-09-16/
        143000.json
        183000.json
    Cebu/
      2026-09-16/
        143005.json
```

Partitioning by city and date is a real pattern used in production data lakes — it makes it cheap to re-process "just Manila's data from last Tuesday" without touching anything else.

## Run it standalone (outside Airflow) to test

```bash
docker compose up -d minio mc-init
export MINIO_ENDPOINT=http://localhost:9000
python3 -m src.extract.fetch_weather
```

## Verify

Open the MinIO console at http://localhost:9001 (login: `minioadmin` / `minioadmin`) and confirm files landed under the `raw-weather` bucket.

Next: [[08-Step-3-Load-to-Warehouse]]
