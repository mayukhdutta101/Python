# To find the sum of square root of any three numbers. 

import math

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

d = math.sqrt(a)+ math.sqrt(b)+ math.sqrt(c)
print(f"Square root of sum of {a}, {b}, {c} is: {d}")