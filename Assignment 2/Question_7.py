# WAP to reverse a given string

def reverse(string):
    reversed_string= " "
    for i in string:
        reversed_string = i + reversed_string
    return reversed_string

string = input("Enter a string: ")

reverse_string = reverse(string)

print("Reversed string is: ", reverse_string)

#Another way

# string = input("Enter a string: ")
# reverse = string[::-1]
# print(reverse)