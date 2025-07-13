import numpy as np 
from datetime import datetime

# creating datetime array using dtype=datetime64
dates = np.array(["2025-06-11", "2025-06-10"], dtype="datetime64")

print(dates)

# datetime array using np.datetime64()
# np.datetime64(datetime_string, unit)
date1 = np.datetime64("2025-06-11")
date2 = np.datetime64("2025-06-10")

dt = np.array([date1, date2])

print(date1)
print(date2)
print(dt)

# Creating Datetime Arrays with Specific Frequencies
dates_fr = np.arange("2025-06-11", "2025-07-01", dtype="datetime64") # creates date array from date 2025-06-11 to 2025-07-01
print(dates_fr)

# creating time array
time_arr = np.arange(np.datetime64("2025-06-11T11:00"), np.datetime64("2025-06-11T14:00"), np.timedelta64(1, "h")) # creates time array from 11:00 to 14:00 with the interval of 1 hour
print(time_arr)

# todays datetime
now = np.datetime64(datetime.now())
print(now)

# comparing dates
print(date1 == date2) # checks if 2 time is equal
print(date1 > date2) # checks if date1 is greater than date2

# datetime arithmetic operation
extra = np.timedelta64(10, "D") # 10 days
print(now + extra) # adds 10 days
print(now - extra) # substracts 10 days

before_1year = np.datetime64("2025-06-13")
today = np.datetime64("2024-07-13")
duration = before_1year - today
print(duration)

print(duration * 2) # multiply by 2
print(duration / 2) # divide by 2