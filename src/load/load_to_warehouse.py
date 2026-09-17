"""
Load layer.

Reads today's raw JSON files out of the data lake (MinIO) and inserts the
fields we need into a staging table in the warehouse (Postgres). This is
the same pattern as loading from S3 into Redshift/Snowflake/BigQuery.

Idempotent by design: `source_file` is UNIQUE and inserts use
ON CONFLICT DO NOTHING, so re-running this script (e.g. after an Airflow
retry) never creates duplicate rows.
"""
import json
from datetime import datetime, timezone

from src.utils.minio_client import get_minio_client, BUCKET_NAME
from src.utils.db import get_connection

CREATE_TABLE_SQL = """
CREATE SCHEMA IF NOT EXISTS raw;
CREATE TABLE IF NOT EXISTS raw.weather_readings (
    id SERIAL PRIMARY KEY,
    city TEXT NOT NULL,
    fetched_at TIMESTAMPTZ NOT NULL,
    temperature NUMERIC,
    windspeed NUMERIC,
    winddirection NUMERIC,
    weathercode INTEGER,
    source_file TEXT UNIQUE,
    raw_payload JSONB,
    loaded_at TIMESTAMPTZ DEFAULT now()
);
"""

INSERT_SQL = """
INSERT INTO raw.weather_readings
    (city, fetched_at, temperature, windspeed, winddirection, weathercode, source_file, raw_payload)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (source_file) DO NOTHING;
"""


def list_today_files():
    client = get_minio_client()
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    paginator = client.get_paginator("list_objects_v2")
    keys = []
    for page in paginator.paginate(Bucket=BUCKET_NAME, Prefix="raw/"):
        for obj in page.get("Contents", []):
            if f"/{today}/" in obj["Key"]:
                keys.append(obj["Key"])
    return keys


def read_object(key):
    client = get_minio_client()
    obj = client.get_object(Bucket=BUCKET_NAME, Key=key)
    return json.loads(obj["Body"].read())


def main():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(CREATE_TABLE_SQL)
    conn.commit()

    keys = list_today_files()
    loaded = 0
    for key in keys:
        record = read_object(key)
        current = record["payload"].get("current_weather", {})
        cur.execute(
            INSERT_SQL,
            (
                record["city"],
                record["fetched_at"],
                current.get("temperature"),
                current.get("windspeed"),
                current.get("winddirection"),
                current.get("weathercode"),
                key,
                json.dumps(record["payload"]),
            ),
        )
        loaded += 1
    conn.commit()
    cur.close()
    conn.close()
    print(f"Loaded {loaded} file(s) into raw.weather_readings")


if __name__ == "__main__":
    main()
