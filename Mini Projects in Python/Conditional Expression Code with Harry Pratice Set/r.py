a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

if((a%2)== 0 and (b%2)== 0 ):
    print("Both of them are even")
elif((a%2)== 0 or (b%2)== 0 ):
    print("One of them is even")


if(a != b):
    print("Both numbers are unique")
else:
    print("OOps!! Try again....")