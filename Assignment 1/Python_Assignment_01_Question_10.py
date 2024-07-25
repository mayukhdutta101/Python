# Write a python program to find if a number is an Armstrong number or not.

# Armstrong number --> 153 => [1^3 + 5^3 + 3^3] == 153... Here the order is 3 because no of digits in the number is 3
n = int(input("Enter a number: "))

sum = 0
order = len(str(n))

copy_n = n

while(n>0):
    digit = n%10
    sum = sum + digit**order
    n = n//10

if(sum == copy_n):
    print(f"{copy_n} is an Armstrong number.")
else:
    print(f"{copy_n} is not an Armstrong number.")