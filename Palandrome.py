# Write a program to print the palandrome or not.

name = input("Enter a string: ")
if name == name[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")