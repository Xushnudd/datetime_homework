#Task 7:
#Write a Python program that adds 5 days to the current date and displays the resulting date.
import datetime
current_day = datetime.datetime.today().strftime("%Y.%m.%d")
current_day = datetime.datetime.strptime(current_day, "%Y.%m.%d")
new_day = current_day + datetime.timedelta(days=5)
print(new_day)