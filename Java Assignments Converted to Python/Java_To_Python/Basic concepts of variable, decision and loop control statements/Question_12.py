'''
Write a program to compute the value of Euler's number that is used as the base of 
natural logarithms. Use the following formula.
e= 1+ 1/1! +1 /2! + 1/3! +................ 1/n!
'''

import math

def calculate_euler(n):

  euler = 1.0
  factorial = 1.0
  for i in range(1, n + 1):
    factorial *= i
    euler += 1 / factorial
  return euler

n = int(input("Enter the number of terms: "))

euler_value = calculate_euler(n)

print("Approximate value of Euler's number:", euler_value)
print("Actual value of Euler's number:", math.e)
