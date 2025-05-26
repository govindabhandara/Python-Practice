# Weather API response
weather_data = {
    "city": "New York",
    "temperature": 72.5,
    "unit": "fahrenheit",
    "forecast": ["sunny", "partly cloudy", "rain"],
    "alerts": None
}

print(f"Current temperature in {weather_data['city']}: {weather_data['temperature']}°F")