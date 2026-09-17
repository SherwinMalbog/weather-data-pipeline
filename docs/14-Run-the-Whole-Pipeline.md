# Run the Whole Pipeline, Start to Finish

## One-time setup

If you haven't already done [[05-Prerequisites-and-Setup]], do that first — it covers installing Docker/Git/Python, unzipping the project, turning it into your own GitHub repo, and creating your `.env` and `profiles.yml` files.

From here on, every command below is typed in your terminal, inside the `weather-data-pipeline` folder:

```bash
cd weather-data-pipeline
```

## Start everything

```bash
docker compose up -d --build
```

This one command builds the Airflow image and starts all four services (MinIO, Postgres, Airflow, Metabase) in the background. `-d` means "detached" — it won't lock up your terminal. `--build` is only strictly needed the first time (or after you change `Dockerfile.airflow`/`requirements.txt`); `docker compose up -d` is enough after that.

Wait ~1–2 minutes for Postgres, MinIO, and Airflow to finish initializing.

## Get your Airflow password

```bash
docker compose logs airflow | grep -i password
```

## Trigger a run

Open http://localhost:8080 → find `weather_pipeline` → trigger it manually (don't wait for the daily schedule).

## Watch it work

1. Check the MinIO console (http://localhost:9001) — raw JSON files should appear
2. Check Postgres — `raw.weather_readings` should have new rows
3. Check dbt — `staging.stg_weather` and `marts.fct_daily_weather` should be built
4. Check Metabase (http://localhost:3000) — refresh your dashboard

## Tear down

```bash
docker compose down          # stop everything, keep data
docker compose down -v       # stop everything, delete all data too
```

Next: [[15-Troubleshooting]]
