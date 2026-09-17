# Step 8 — Visualize with Metabase

## Goal

Put a dashboard on top of the `marts` schema so the pipeline produces something a non-technical person could actually look at.

## Start Metabase

```bash
docker compose up -d metabase
```

Open http://localhost:3000 and complete the setup wizard.

## Connect to the warehouse

When asked to add a database:
- Type: PostgreSQL
- Host: `postgres` (the Docker service name, not `localhost`)
- Port: `5432`
- Database: `warehouse`
- Username: `warehouse`
- Password: `warehouse`

## Build one chart

Try: a line chart of `avg_temperature_c` over `reading_date`, grouped by `city`, from `marts.fct_daily_weather`. Save it to a dashboard.

## Why this step matters for your resume

This is what makes the project readable by a Data Analyst or BI Analyst hiring manager, not only a Data Engineer one — see [[16-How-to-Talk-About-This-On-Your-Resume]].

Next: [[14-Run-the-Whole-Pipeline]]
