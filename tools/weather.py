import requests
import os

CACHE = {}

def weather_tool(city: str):
    if city in CACHE:
        return CACHE[city]

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": os.getenv("OPENWEATHER_API_KEY"),
        "units": "metric"
    }

    data = requests.get(url, params=params).json()

    if "main" not in data:
        return {"error": "Weather API failed"}

    result = {
        "temperature": data["main"]["temp"],
        "condition": data["weather"][0]["description"]
    }

    CACHE[city] = result
    return result
