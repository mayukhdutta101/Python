'''
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again

Then, the output should be:
again and hello makes perfect practice world
'''

string = input("Enter a sequence of words: ")
word_list = string.split()
list_to_set = set(word_list)
sort = sorted(list_to_set)
final_output = ' '.join(sort)
print("Sorted words without duplicates: ",final_output)