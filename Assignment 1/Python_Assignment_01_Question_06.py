# Write a python program to print prime number series upto n.

def is_prime(num):
    if(num<=1):
        return False
    for i in range(2, int(num**0.5)+1):
        if(num%i == 0):
            return False
    return True

n = int(input("Enter the range: "))

prime = []

for num in range(2,n+1):
    if(is_prime(num)):
        prime.append(num)

print(f"Prime numbers upto {n} are: {prime}")