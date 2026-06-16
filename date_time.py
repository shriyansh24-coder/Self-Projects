#Date and Time

import datetime
# Get the current date and time
current_datetime = datetime.datetime.now()
print("Current date and time:", current_datetime)

target_date = datetime.datetime(2024, 12, 25)
print("Target date:", target_date)

if target_date < current_datetime:
    print("The target date is past.")
elif target_date > current_datetime:
    print("The target date is in the future.")
else:
    print("The target date is today.")    