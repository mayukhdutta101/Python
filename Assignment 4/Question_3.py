'''
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

Suppose the following input is supplied to the program:
Hello world
Practice makes perfect

Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
'''

lines = []

while True:
    l = input("Enter a line: ")
    if l:
        lines.append(l.upper())
    else:
        break

for l in lines:
    print(l)