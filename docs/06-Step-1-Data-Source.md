# Step 1 — Data Source

## What we're using

[Open-Meteo](https://open-meteo.com) — a free weather API with no API key and no rate-limit registration required for non-commercial use.

## Endpoint

```
GET https://api.open-meteo.com/v1/forecast
    ?latitude={lat}
    &longitude={lon}
    &current_weather=true
    &hourly=temperature_2m,precipitation,wind_speed_10m
    &timezone=auto
```

## Cities tracked

Defined in `config/cities.yaml` — edit this file to track different cities:

```yaml
cities:
  - name: Manila
    lat: 14.5995
    lon: 120.9842
```

## Try it yourself first

Before writing any code, hit the API directly so you know exactly what shape of JSON you're dealing with:

```bash
curl "https://api.open-meteo.com/v1/forecast?latitude=14.5995&longitude=120.9842&current_weather=true"
```

Notice `current_weather` is a flat object with `temperature`, `windspeed`, `winddirection`, `weathercode`. That's exactly what `src/extract/fetch_weather.py` pulls out later.

Next: [[07-Step-2-Extract-to-Data-Lake]]
