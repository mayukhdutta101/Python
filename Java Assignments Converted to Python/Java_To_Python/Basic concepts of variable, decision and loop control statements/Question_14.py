# Write a program to read two integer values m and n and to decide and print whether m is multiple of n.

m = int(input("Enter an integer value: "))
n = int(input("Enter an integer value: "))

if(m%n == 0):
    print(f"{m} is a multiple of {n}")
else:
    print(f"{m} is not a multiple of {n}")