'''
Please write a program which count and print the numbers of each character in a string input by console.

Example:
If the following string is given as input to the program:
abcdefgabc

Then, the output of the program should be:
a,2
c,2
b,2
e,1
d,1
g,1
f,1
'''

string = input("Enter a string: ")
count = {}

for c in string:
    if c in count:
        count[c] += 1
    else:
        count[c] = 1

for c, count in count.items():
    print(f"{c}, {count}")