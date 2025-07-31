import pywhatkit as pwk
from datetime import datetime

phone_number = "+91 9631412596"
message = "Your phone is hacked"
now = datetime.now()
hour = now.hour
minute = now.minute + 2  # Schedule the message to be sent 2 minutes from now

# Ensure that the minute does not exceed 59
if minute >= 60:
    minute -= 60
    hour += 1

pwk.sendwhatmsg(phone_number, message, hour, minute)