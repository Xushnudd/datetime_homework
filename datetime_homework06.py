#Task 6:
#Write a Python program that accepts a date in the format "dd-mm-yyyy" and checks if it is a leap year. Display an appropriate message indicating whether it is a leap year or not.
import datetime

user_input = input("Sanani dd-mm-yyyy formatda kiriting: ")
d = datetime.datetime.strptime(user_input, "%d-%m-%Y")
year = d.year
if (year % 4 == 0):
    print(f"{year} yili kabisa yil.")
else:
    print(f"{year} yili kabisa yil emas.")