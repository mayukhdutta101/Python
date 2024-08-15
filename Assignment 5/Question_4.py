'''
Create a set given below

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

I.Find the length of the set it_companies
II.Add 'Twitter' to it_companies
III.Insert multiple IT companies at once to the set it_companies
IV.Remove one of the companies from the set it_companies
V.What is the difference between remove and discard
'''

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# I.Find the length of the set it_companies
print(f"Length of the set it_companies is: {len(it_companies)}")

# II.Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(f"After adding 'Twitter' to the set it_companies:-\n{it_companies}")

# III.Insert multiple IT companies at once to the set it_companies
to_be_added = ['Accenture','Cognizant','Meta']
it_companies.update(to_be_added)
print(f"Updated set it_companies:-\n{it_companies}")

# IV.Remove one of the companies from the set it_companies
it_companies.remove('Oracle')
print(f"After removing 'Oracle' from the set it_companies:-\n{it_companies}")

# V.What is the difference between remove and discard
#Ans> Both remove and discard methods in python are used to remove a specific element from a set. But 'remove' method raises a KeyError if the element is not found within the set, while discard method does not raise any error when the desired element is not found within the set.