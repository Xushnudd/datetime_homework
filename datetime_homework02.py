#Task 2:
#Write a Python program to get the current year.
import datetime

now = datetime.datetime.now()
print(now.strftime("%Y"))