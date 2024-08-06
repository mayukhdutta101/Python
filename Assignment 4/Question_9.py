'''
Write a program that accepts a string

1.reverses it.
2.checks whether it is a palindrome.
3.checks whether it ends with a specific substring.
4.capitalize the first letter of each word in a string
5.check if a string is anagram of another string
6.remove vowels from string
7.find length of the longest word in a sentence
'''

# Accepting input strings
input_string = input("Enter a string: ")
substring_to_check = input("Enter the substring to check for ending: ")
anagram_string1 = input("Enter the first string for anagram check: ")
anagram_string2 = input("Enter the second string for anagram check: ")
sentence = input("Enter a sentence: ")

# 1. Reverse the string
reversed_string = input_string[::-1]
print(f"Reversed String: {reversed_string}")

# 2. Check if the string is a palindrome
is_input_palindrome = input_string == reversed_string
print(f"Is palindrome: {is_input_palindrome}")

# 3. Check if the string ends with a specific substring
ends_with_substring = input_string.endswith(substring_to_check)
print(f"Ends with '{substring_to_check}': {ends_with_substring}")

# 4. Capitalize the first letter of each word in the string
capitalized_string = input_string.title()
print(f"Capitalized String: {capitalized_string}")

# 5. Check if two strings are anagrams
are_anagrams = sorted(anagram_string1) == sorted(anagram_string2)
print(f"Are anagrams: {are_anagrams}")

# 6. Remove vowels from the string
vowels = "aeiouAEIOU"
string_without_vowels = ''.join(char for char in input_string if char not in vowels)
print(f"String without vowels: {string_without_vowels}")

# 7. Find the length of the longest word in a sentence
words = sentence.split()
longest_length = max(len(word) for word in words) if words else 0
print(f"Length of the longest word: {longest_length}")
