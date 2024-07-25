# Write a program to count the number of digits of an integer.

def count_digits(num):
    count = 0
    while(num>0):
        num //= 10
        count+=1
    return count

n = int(input("Enter a number: "))
print(f"Number of digits in {n} are: {count_digits(n)}")
