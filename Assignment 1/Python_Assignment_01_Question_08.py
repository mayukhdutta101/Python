# Write a python program to find if a number is palindrome or not.

def is_palindrome(n):
    original = n
    rev = 0

    while n > 0:
        rem = n % 10
        rev = (rev * 10) + rem
        n = n // 10
    return rev == original

n = int(input("Enter a number: "))
if is_palindrome(n):
    print("Palindrome")
else:
    print("Not Palindrome")


