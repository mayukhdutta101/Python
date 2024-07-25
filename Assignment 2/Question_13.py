# Write a Python program to print the first 6 terms of a geometric sequence starting with 2 and having a common ratio of 3

start = 2
ratio = 3
num_terms = 6

for i in range(num_terms):
    term = start * (ratio ** i)
    print(term, end=" ")
