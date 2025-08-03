# Write a program in  the list find the even and odd numbers

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []

for i in num:
    if i % 2 == 0:
        even_numbers.append(i)
odd_numbers = []
for i in num:
    if i % 2 != 0:
        odd_numbers.append(i)
print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)