# Write a Program to check if a number is Positive or Negative

n = int(input("Enter a number: "))
if(n<0):
    print(f"{n} is negative.")
elif(n>0): 
    print(f"{n} is positive.")
else:
    print(f"{n} is neutral.")