# Print the series upto N terms: 1,2,6,24,120,720 …

def fact(n):
    if(n==0):
        return 1
    else:
        return n * fact(n-1)
    
n = int(input("Enter the terms: "))
for i in range(1,n+1):
    print(fact(i), end= " ")