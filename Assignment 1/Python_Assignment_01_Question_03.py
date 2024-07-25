# Write a python program to find if a year is a leap year or not.

year = int(input("Enter a year: "))

if(year%4==0 or (year%100!=0 and year%400==0)):
    print(f"{year} is leap year.")
else:
    print(f"{year} is not a leap year.")