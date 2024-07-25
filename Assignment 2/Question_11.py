# Write a program in Python to find the sum of digits of a number.

def getSum(n): 
    
    sum = 0
    while (n != 0): 
        sum = sum + (n % 10)
        n = n//10
       
    return sum
   
n = int(input("Enter a number: "))
print(f"Sum of digits of {n} is: {getSum(n)}")