# Write a program to check whether a number is Buzz or not.

n = int(input("Enter a number: "))

if(n%7==0 or n%10==7):
    print(f"{n} is a Buzz number.")
else:
    print(f"{n} is not a buzz number.")