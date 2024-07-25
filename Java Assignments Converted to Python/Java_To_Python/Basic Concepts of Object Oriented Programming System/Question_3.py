# Write a program to change temperature from Fahrenheit to Celsius.

temp = int(input("Enter the temperature in fahrenheit: "))

c = (temp - 32) * (5/9)

print(f"Temperature in celsius is: {c}")