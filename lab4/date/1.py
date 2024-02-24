#Write a Python program to subtract five days from current date.

import datetime

def FiveDaysAgo():
    current = datetime.datetime.now()
    new = current.day - 5
    return new

print(FiveDaysAgo())
#a