#Write a Python program to calculate two date difference in seconds.

import datetime

date1 = datetime.datetime.today()
date2 = datetime.datetime(2003, 4, 24)
diff = date1 - date2
print(f"Difference beetween 2 dates in seconds: {diff.total_seconds()}")