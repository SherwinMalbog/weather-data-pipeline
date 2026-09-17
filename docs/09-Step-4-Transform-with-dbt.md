# Step 4 — Transform with dbt

## Goal

Turn raw, semi-structured rows into clean, tested, documented tables that a BI tool or an analyst can query directly.

## Project layout

```
dbt_project/
  models/
    staging/
      stg_weather.sql       -- cleans + types the raw table
      schema.yml             -- source definition + tests
    marts/
      dim_city.sql            -- city reference table (from seed)
      fct_daily_weather.sql   -- daily aggregated metrics per city
      schema.yml               -- tests
  seeds/
    cities.csv                -- static reference data
```

## The staging → marts pattern

- **staging**: one-to-one with the source table, just cleaned and typed. No business logic.
- **marts**: the tables people actually query — aggregated, joined, business-friendly names.

This two-layer pattern (some teams add a third, "intermediate," layer) is close to universal in dbt projects — learn it once, recognize it in every dbt codebase you'll ever open.

## Run it

```bash
cd dbt_project
dbt seed
dbt run
dbt test
```

## See what dbt actually built

```bash
dbt docs generate
dbt docs serve
```

This spins up a browsable, auto-generated documentation site with a dependency graph (the "DAG" of your models) — a good thing to screenshot for your portfolio.

Next: [[10-Step-5-Orchestrate-with-Airflow]]
