#Task 5:
#Write a Python program that prompts the user to enter a specific date in the format "dd-mm-yyyy" and determines the day of the week on which that date falls.
import datetime

user_input = input("Sanani dd-mm-yyyy formatda kiriting: ")
d = datetime.datetime.strptime(user_input, "%d-%m-%Y")
d = datetime.datetime.strftime(d, "%A")
print(d)