# Write a program to find maximum of three numbers

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

if(a>b and a>c):
    print(f"{a} is largest.")
elif(b>a and b>c):
    print(f"{b} is largest.")
else:
    print(f"{c} is largest.")