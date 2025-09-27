# Write a program to print the otp if user input otp get sucessfull responce.

import random

x = random.randint(100000,999999)
print(x)

user_input = int(input("Enter a otp : "))

if user_input == x:
    print("Login sucessfully!")
else:
    print("Login unsucessfully! try again later")
