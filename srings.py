# Write a python program to find the uppercase letters and lowercase letters in a given string.


string= input("Enter a string: ")
uppercase_count = 0
lowercase_count = 0
for char in string:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
print("Uppercase letters:", uppercase_count)
print("Lowercase letters:", lowercase_count)