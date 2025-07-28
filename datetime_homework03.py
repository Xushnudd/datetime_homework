#Task 3:
#Write a Python program that prompts the user to enter a specific date in the format "dd-mm-yyyy" and calculates the number of days between the current date and the entered date.
import datetime

user_input = input("Sanani dd-mm-yyyy formatda kiriting: ")
d = datetime.datetime.strptime(user_input, "%d-%m-%Y")
b = datetime.datetime.now().strftime("%d-%m-%Y")
b = datetime.datetime.strptime(b, "%d-%m-%Y")

if d>b:
    print(d-b)
else:
    print(b-d)