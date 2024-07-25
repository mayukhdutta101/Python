#Write a python program to find if a number is a perfect number or not.

def is_perfect_number(n):
    divisors = []
    for i in range(1, n):
        if(n%i==0):
            divisors.append(i)
    
    add = sum(divisors)
    return add


n = int(input("Enter a number: "))
if(is_perfect_number(n) == n):
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")