# Write a program to find HCF of two Numbers.

def is_hcf(x,y):
    
    if(x>y):
        smaller = y
    else:
        smaller = x
    
    for i in range (1,(smaller+1)):
        if(x%i==0 and y%i==0):
            hcf = i
    return hcf

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"HCF of {a} & {b} is: {is_hcf(a,b)}")

