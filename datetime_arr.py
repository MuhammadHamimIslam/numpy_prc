import numpy as np 

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