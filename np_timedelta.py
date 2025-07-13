import numpy as np
import datetime

# Date Arithmetic with datetime64
date = np.datetime64("2025-07-13")
print(date)

# add days to initial day
date_after10 = date + np.timedelta64(10, "D") # adds 10 days to initial
print(date_after10)

# # Subtract month from the initial date by converting to datetime and using a timedelta
date_as_datetime = date.astype(np.datetime64) # convert to datetime
sub_month = date_as_datetime - datetime.timedelta(days=30) # assume 1 month = 30 days
print(sub_month)

# Converting between datetime64 and timedelta64
start_day = np.datetime64("2025-06-16")
end_day = np.datetime64("2025-08-02")

duration = end_day - start_day
print(duration)
new_date = start_day + duration # Converting timedelta64 to datetime64
print(new_date)
