#Task 10:
#Write a Python program that converts a given timestamp to a readable date and time format. Prompt the user to enter a timestamp (number of seconds since the Unix epoch) and display the corresponding date and time.
import datetime
user_input = input("Unix vaqtini soniyalarda kiriting: ")
timestamp = datetime.date.fromtimestamp(float(user_input))
print(timestamp)