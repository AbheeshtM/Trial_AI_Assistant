import requests
import re

# 🔑 Your OpenWeather API key
OPENWEATHER_API_KEY = "36dcef5cdb333bfc594d0721d83154e0"

# 🌆 Fallback city if no city is found in query
DEFAULT_CITY = "Lucknow"

# 🏙️ Extract city from query using simple pattern match
def extract_city(text):
    # Match city names assuming format like: "weather in Delhi" or "Bhopal ka mausam"
    match = re.search(r"(?:in|at|ka|ke|ki)\s+([A-Za-z\u0900-\u097F\s]+)", text, re.IGNORECASE)
    if match:
        city = match.group(1).strip()
        return city
    return None

# 🌦️ Get weather from OpenWeatherMap
def get_weather(user_query: str) -> str:
    city = extract_city(user_query) or DEFAULT_CITY
    print(f"📍 Fetching weather for: {city}")

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": OPENWEATHER_API_KEY,
            "units": "metric"
        }
        response = requests.get(url, params=params)
        data = response.json()

        if data.get("cod") != 200:
            print("⚠️ Weather API error:", data.get("message", "Unknown error"))
            return "I couldn't fetch the weather right now. Please try again later."

        weather = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]

        return f"The weather in {city} is {weather}, with a temperature of {temp}°C, feels like {feels_like}°C, and humidity at {humidity}%."

    except Exception as e:
        print("❌ Error in get_weather():", str(e))
        return "Sorry, I couldn't fetch the weather right now."
