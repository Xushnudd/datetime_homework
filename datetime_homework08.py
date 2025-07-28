#Task 8:
#Write a Python program that subtracts 10 hours from the current time and displays the resulting time.
import datetime
current_hour = datetime.datetime.now().hour
new_hour = current_hour - 10
print(new_hour)