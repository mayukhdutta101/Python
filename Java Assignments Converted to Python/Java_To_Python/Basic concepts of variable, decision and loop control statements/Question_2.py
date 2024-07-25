# Write a program to calculate factorial of 12

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
factorial= fact(12)
print(factorial)