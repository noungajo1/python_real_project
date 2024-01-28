#Getting the current date and time
from datetime import datetime

current_datetime = datetime.now()
print("Current Date and Time:", current_datetime)
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date and Time:", formatted_datetime)