from datetime import datetime
import pytz

# Supported cities with timezone mapping
CITY_TIMEZONES = {
    "lucknow": "Asia/Kolkata",
    "delhi": "Asia/Kolkata",
    "mumbai": "Asia/Kolkata",
    "kolkata": "Asia/Kolkata",
    "new york": "America/New_York",
    "london": "Europe/London",
    "tokyo": "Asia/Tokyo",
    "sydney": "Australia/Sydney",
    "paris": "Europe/Paris"
}

def get_date_time_by_city(text, only_date=False):
    for city in CITY_TIMEZONES:
        if city in text.lower():
            tz = pytz.timezone(CITY_TIMEZONES[city])
            now = datetime.now(tz)
            date_str = now.strftime("%d-%m-%Y")
            day = now.strftime("%A")
            if only_date:
                return f"The date in {city.title()} is {date_str} ({day})."
            else:
                time_str = now.strftime("%I:%M %p")
                return f"The time in {city.title()} is {time_str} on {day}, {date_str}."

    # Default: India
    tz = pytz.timezone("Asia/Kolkata")
    now = datetime.now(tz)
    date_str = now.strftime("%d-%m-%Y")
    day = now.strftime("%A")
    if only_date:
        return f"Today's date is {date_str} ({day})."
    else:
        time_str = now.strftime("%I:%M %p")
        return f"The current time is {time_str} on {day}, {date_str}."
