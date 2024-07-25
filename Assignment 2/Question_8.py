# Write a function to calculate the power of a number using recursion

def power(base, exponent):
    if(exponent==0):
        return 1
    else:
        return (base * power(base,exponent-1))
    
base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

print(f"{base} to the power of {exponent} is: {power(base,exponent)}")