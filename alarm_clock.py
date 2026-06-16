#Working Alarm Clock

import time
import datetime
# Set the alarm time (24-hour format)
alarm_time = input("Enter the alarm time (HH:MM): ")
# Validate the input format
try:
    alarm_hour, alarm_minute = map(int, alarm_time.split(':'))
    if not (0 <= alarm_hour < 24 and 0 <= alarm_minute < 60):
        raise ValueError
except ValueError:
    print("Invalid time format. Please enter time in HH:MM format.")
    exit()
print(f"Alarm set for {alarm_time}.")
while True:
    current_time = datetime.datetime.now().strftime("%H:%M")
    if current_time == alarm_time:
        print("Wake up! It's time!")
        break
    time.sleep(10)  # Check every 10 seconds    