# Write a Python code calculator program

a = int(input("Enter a value:"))
b = int(input("Enter a value:"))
opr = input("Enter a operator : ")

if opr =="+":
    print("Result:", a+b)
elif opr =="-":
    print("Result:", a-b)
elif opr =="*":
    print("Result:", a*b)
elif opr =="/":
    print("Result:", a/b)
else:
    print("Invalid operator!")
