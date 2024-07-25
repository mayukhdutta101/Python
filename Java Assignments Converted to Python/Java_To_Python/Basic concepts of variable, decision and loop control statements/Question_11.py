# Write a program to find median of a set of numbers.

import statistics

def find_median(a, b):
    numbers = list(range(a,b+1))
    return statistics.median(numbers)

a = int(input("Enter the lower limit: "))
b = int(input("Enter the upper limit: "))

print(f"Median of {a} & {b} is: {find_median(a,b)}")