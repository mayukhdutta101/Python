# Write a program to print all multiple of 10 between a given interval

a = int(input("Enter the starting range: "))
b = int(input("Enter the ending range: "))

for i in range(a,b+1):
    if(i%10==0):
        print(i)