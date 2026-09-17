-- One-to-one with the raw source table: cleaned and typed, no business logic.
-- See docs/09-Step-4-Transform-with-dbt.md for the staging vs. marts pattern.

with source as (
    select * from {{ source('raw', 'weather_readings') }}
)

select
    id as reading_id,
    city,
    fetched_at,
    temperature::numeric as temperature_c,
    windspeed::numeric as windspeed_kmh,
    winddirection::numeric as wind_direction_deg,
    weathercode::int as weather_code,
    loaded_at
from source
