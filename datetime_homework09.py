#Task 9:
#Write a Python program that calculates the difference between two given dates. Prompt the user to enter two dates in the format "dd-mm-yyyy" and display the number of days between them.
import datetime

user_input = input("Sanani dd-mm-yyyy formatda kiriting: ")
d = datetime.datetime.strptime(user_input, "%d-%m-%Y")
user_input = input("Sanani dd-mm-yyyy formatda kiriting: ")
b = datetime.datetime.strptime(user_input, "%d-%m-%Y")

if d>b: print(d-b)
else: print(b-d)
