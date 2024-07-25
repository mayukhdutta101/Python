#Write a python program to reverse a number.

n = int(input("Enter a number: "))

rev = 0

while(n>0):
    rem = n%10
    rev = (rev*10)+rem
    n=n//10 # // means integer division.
    

print(f"Reversed number of {n} is : {rev}")