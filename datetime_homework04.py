#Task 4:
#Write a Python program that calculates the age of a person based on their birth year. Prompt the user to enter their birth year, and display their current age.
import datetime

user_input = input("Qaysi yili to'g'ilgansiz: ")
current_year = datetime.datetime.now().year
birth_year = int(user_input)
age = current_year - birth_year
print(f"Sizning yoshingiz: {age} yosh")