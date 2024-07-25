# Write a Python program that prompts the user to enter a base number and an exponent, and then calculates the power of the base to the exponent. The program should not use the exponentiation operator (**) or the math.pow() function.

base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

result = 1
for i in range(exponent):
    result *= base
    
print(f"{base} to the power {exponent} is: {result}")