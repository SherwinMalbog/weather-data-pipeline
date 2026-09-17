-- City reference/dimension table, sourced from the seed file.
select
    city_name,
    country,
    latitude,
    longitude
from {{ ref('cities') }}
