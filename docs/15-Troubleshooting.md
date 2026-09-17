# Troubleshooting

### `dbt` can't connect to Postgres
Check `dbt_project/profiles.yml` exists (copied from `.example`) and its host matches where you're running dbt from: `postgres` (inside Docker) vs `localhost` (on your host machine).

### MinIO bucket doesn't exist / "NoSuchBucket" error
The `mc-init` service creates the bucket on first startup. Run `docker compose up -d mc-init` again, or create it manually at http://localhost:9001.

### Airflow webserver won't load / "unhealthy" container
Give it another minute — first boot runs database migrations. Check `docker compose logs airflow`.

### "relation raw.weather_readings does not exist" when running the load script
Run the load script once — it creates the table itself on first run (see `CREATE_TABLE_SQL` in `load_to_warehouse.py`).

### Port already in use (5432, 8080, 9000, 9001, 3000)
Something else on your machine is using that port. Either stop it, or change the left-hand side of the port mapping in `docker-compose.yml` (e.g. `"5433:5432"`).

### Everything's a mess and you just want to start clean

```bash
docker compose down -v
docker compose up -d --build
```

Next: [[16-How-to-Talk-About-This-On-Your-Resume]]
