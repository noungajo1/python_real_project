from datetime import datetime, timedelta

date_string = "2022-01-28 12:30:45"
parsed_datetime = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed Date and Time:", parsed_datetime)

#Adding 1 day to the current date and time
current_datetime = datetime.now()
new_datetime = current_datetime + timedelta(days=1)
print("New Date and Time:", new_datetime)