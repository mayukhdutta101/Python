# Write a program to enter a string. Calculate the length of the string. Find the substring country. Count the occurences of each word in the given sentence.
# If the String as input is India is my motherland. I love my country. Capital of India is New Delhi.

string = input("Enter a string: ")
print(f"Length of the given string is: {len(string)}")
substring_pos = string.find("country")
if (substring_pos != -1):
    print(f"\"country\" was found at index: {substring_pos}")
else:
    print(f"\"country\" was not foung in the given string!!")

words = string.split()
count_word = {}
for word in words:
    count_word[word] = count_word.get(word, 0) + 1

print("Occurences of each word:- ")
print(f"'{word}': {count_word}")