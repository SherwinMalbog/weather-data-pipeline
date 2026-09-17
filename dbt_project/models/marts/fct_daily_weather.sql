-- Daily aggregated weather metrics per city -- the table a dashboard queries.
select
    city,
    date_trunc('day', fetched_at) as reading_date,
    round(avg(temperature_c), 1) as avg_temperature_c,
    round(min(temperature_c), 1) as min_temperature_c,
    round(max(temperature_c), 1) as max_temperature_c,
    round(avg(windspeed_kmh), 1) as avg_windspeed_kmh,
    count(*) as reading_count
from {{ ref('stg_weather') }}
group by 1, 2
