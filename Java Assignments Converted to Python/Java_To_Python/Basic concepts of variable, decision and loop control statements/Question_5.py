# Write a program to generate multiplication table

n = int(input("Enter a number: "))

for i in range(1,11):
    print(f"{n} * {i} = {n*i}")