#Write a program to print the numbers from 1 to 100.

num = [i for i in range(1, 101)]
print(num)

# To above output print odd numbers only
odd_num = [i for i in num if i % 2 != 0]
print(odd_num)

# To above output print even numbers only
even_num = [i for i in num if i % 2 == 0]
print(even_num)