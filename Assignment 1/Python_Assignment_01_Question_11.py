# Write a python program to print Fibonacci series upto n.

n = int(input("Enter the number of terms: "))

a = 0
b = 1
print("Fibonacci Series:", end=" ")

for _ in range(n):
    print(a, end=" ")
    c = a+b
    a = b
    b = c

