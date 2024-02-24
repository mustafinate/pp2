#Write a Python program to print yesterday, today, tomorrow.

import datetime

today = datetime.datetime.now()

print("Yesterday: ", today.day - 1)
print("Today: ", today.day)
print("Tomorrow: ", today.day + 1)