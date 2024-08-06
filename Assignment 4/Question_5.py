'''
Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:
hello world! 123

Then, the output should be:
LETTERS 10
DIGITS 3
'''

import re
string = input("Enter a sentence: ")

letters = re.findall(r'[a-zA-Z]', string)
digits = re.findall(r'\d', string)

print(f"LETTERS {len(letters)}")
print(f"DIGITS {len(digits)}")
