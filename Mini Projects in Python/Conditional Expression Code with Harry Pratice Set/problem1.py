# Write a program to find the greatest of four numbers entered by the user.

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
d = int(input("Enter a number: "))

if(a>b & a>c & a>d):
    print(f"{a} is greatest")
elif(b>a & b>c & b>d):
    print(f"{b} is greatest")
elif(c>a & c>b & c>d):
    print(f"{c} is greatest")
else:
    print(f"{d} is greatest")