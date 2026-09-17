"""
Unit test for the extract layer -- mocks the Open-Meteo API so tests never
depend on network access or real API responses.
"""
import responses

from src.extract.fetch_weather import fetch_city_weather, API_URL


@responses.activate
def test_fetch_city_weather_returns_json():
    fake_response = {"current_weather": {"temperature": 27.4, "windspeed": 10.1}}
    responses.add(responses.GET, API_URL, json=fake_response, status=200)

    city = {"name": "TestCity", "lat": 1.0, "lon": 1.0}
    result = fetch_city_weather(city)

    assert result == fake_response


@responses.activate
def test_fetch_city_weather_raises_on_http_error():
    responses.add(responses.GET, API_URL, json={"error": "boom"}, status=500)

    city = {"name": "TestCity", "lat": 1.0, "lon": 1.0}

    try:
        fetch_city_weather(city)
        assert False, "expected an HTTPError to be raised"
    except Exception as e:
        assert "500" in str(e)
