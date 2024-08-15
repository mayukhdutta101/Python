'''
Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

I.Get the length of the student dictionary
II.Get the value of skills and check the data type, it should be a list
III.Modify the skills values by adding one or two skills
IV.Get the dictionary keys as a list
V.Get the dictionary values as a list
VI.Change the dictionary to a list of tuples using _items()_ method
VII.Delete one of the items in the dictionary
VIII.Delete one of the dictionaries
'''

student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 21,
    'marital_status': 'Single',
    'skills': ['Python', 'JavaScript'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main St'
}

# I. Get the length of the student dictionary
len_dict = len(student)
print("Length of student dictionary:", len_dict)

# II. Get the value of skills and check the data type
skills = student['skills']
print("Skills:", skills)
print("Data type of skills:", type(skills))

# III. Modify the skills values by adding one or two skills
student['skills'].extend(['HTML', 'CSS'])
print("Updated skills:", student['skills'])

# IV. Get the dictionary keys as a list
keys_list = list(student.keys())
print("Dictionary keys:", keys_list)

# V. Get the dictionary values as a list
values_list = list(student.values())
print("Dictionary values:", values_list)

# VI. Change the dictionary to a list of tuples using items() method
items_list = list(student.items())
print("Dictionary as list of tuples:", items_list)

# VII. Delete one of the items in the dictionary
del student['address']
print("Dictionary after deleting 'address':", student)

# VIII. Delete the entire dictionary
del student

try:
    print(student)
except NameError:
    print("The student dictionary has been deleted.")
