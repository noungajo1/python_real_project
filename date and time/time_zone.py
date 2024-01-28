import datetime
import pytz # we need to install pytz library

#Get the current time in UTC
utc_now = datetime.datetime.now(pytz.utc)
print("Current UTC Time:",utc_now)

#Convert UTC time to a specific time zone
desired_timezone = pytz.timezone("America/New_York")
local_time = utc_now.astimezone(desired_timezone)
print("Local Time in New York:", local_time)