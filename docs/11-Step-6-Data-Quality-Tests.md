# Step 6 — Data Quality Tests

## Why this matters

"The pipeline ran successfully" and "the data is correct" are different claims. Data quality tests catch the second one.

## Tests already in this project

Defined in `dbt_project/models/**/schema.yml`:
- `not_null` — a column should never be empty (e.g. `city`, `temperature_c`)
- `unique` — a column should have no duplicates (e.g. `reading_id`, `city_name`)

## Run just the tests

```bash
cd dbt_project
dbt test
```

A failing test doesn't stop your data from loading — it flags a problem for you to investigate. That's the point: tests are a smoke detector, not a fire door.

## Add your own test

Try adding an `accepted_values` test on `weather_code` (Open-Meteo returns integer codes 0–99) or a custom SQL test that checks `min_temperature_c <= max_temperature_c` in `fct_daily_weather`. Documenting a test *you* added, and why, is a great interview talking point.

Next: [[12-Step-7-CI-CD]]
