# Write a Python program to calculate two date difference in seconds.

import datetime

data1 = datetime.datetime.now()
data2 = datetime.datetime(2022, 1, 1, 3, 4, 4)

delta = (data1 - data2)
print(delta.total_seconds())
