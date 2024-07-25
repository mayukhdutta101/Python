# Write a program in Python that prompts the user to input a number and prints its  multiplication table.

n = int(input("Enter a number: "))

for i in range(1,11):
    print(f"{n} * {i} = {n*i}")