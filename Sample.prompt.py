# Write a program to do not print the not repeated srting.

# naa = "Abbccdefgh"

# for i in naa:
#     if naa.count(i)==1:
#         print(i,end="")
        
#===================================================================#

# Write a program to example for shallow copy

na = [1,2,3,4]

def foo(x):
    x.append(5)
    return x



print(foo(na.copy()))
print(na)
    