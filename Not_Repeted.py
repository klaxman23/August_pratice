#Write a program to print the not repeted characters in a string

nn = input("Enter a string: ")

for i in nn:
    if nn.count(i) == 1:
        print(i, end="")