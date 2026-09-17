"""
Extract layer.

Pulls current weather data from the free Open-Meteo API for every city in
config/cities.yaml, and lands the raw JSON response in the data lake (MinIO)
completely unchanged.

Design decision: this script never transforms data. It only fetches and
stores. See docs/04-Design-Decisions.md (ADR-01) for why raw data is kept
separate from transformation logic.
"""
import io
import json
import os
from datetime import datetime, timezone

import requests
import yaml

from src.utils.minio_client import get_minio_client, BUCKET_NAME

CONFIG_PATH = os.environ.get("CITIES_CONFIG", "config/cities.yaml")
API_URL = "https://api.open-meteo.com/v1/forecast"


def load_cities():
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)["cities"]


def fetch_city_weather(city):
    params = {
        "latitude": city["lat"],
        "longitude": city["lon"],
        "current_weather": "true",
        "hourly": "temperature_2m,precipitation,wind_speed_10m",
        "timezone": "auto",
    }
    response = requests.get(API_URL, params=params, timeout=30)
    response.raise_for_status()
    return response.json()


def upload_raw(city_name, payload):
    client = get_minio_client()
    now = datetime.now(timezone.utc)
    key = f"raw/{city_name}/{now.strftime('%Y-%m-%d')}/{now.strftime('%H%M%S')}.json"
    body = json.dumps(
        {
            "city": city_name,
            "fetched_at": now.isoformat(),
            "payload": payload,
        }
    ).encode("utf-8")
    client.put_object(
        Bucket=BUCKET_NAME, Key=key, Body=io.BytesIO(body), ContentLength=len(body)
    )
    return key


def main():
    cities = load_cities()
    uploaded = []
    for city in cities:
        payload = fetch_city_weather(city)
        key = upload_raw(city["name"], payload)
        uploaded.append(key)
        print(f"Uploaded {key}")
    return uploaded


if __name__ == "__main__":
    main()
