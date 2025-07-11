from datetime import datetime
import pytz

def get_current_time_ist():
    now = datetime.now(pytz.timezone("Asia/Kolkata"))
    return now.strftime("%I:%M %p")
