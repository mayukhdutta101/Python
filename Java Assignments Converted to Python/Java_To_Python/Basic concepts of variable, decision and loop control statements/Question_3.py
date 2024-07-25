'''
Admission to a professional course is subject to the following conditions:
(a) marks in Mathematics >= 60 (b) marks in Physics >=50
(c) marks in Chemistry >=40 (d) Total in all 3 subjects >=200
 (Or)
 Total in Maths & Physics>=150
Given the marks in the 3 subjects of n (user input) students, write a program to process 
the applications to list the eligible candidates
'''

def is_eligible(maths, phys, chem):

  return (maths >= 60 and phys >= 50 and chem >= 40 and (maths + phys + chem >= 200 or maths + phys >= 150))

def process_applications(n):

  eligible_students = []
  for _ in range(n):
    name = input("Enter name of the student: ")
    maths = int(input("Enter the marks in mathematics: "))
    phys = int(input("Enter the marks in physics: "))
    chem = int(input("Enter the marks in chemistry: "))

    if is_eligible(maths, phys, chem):
      eligible_students.append(name)

  print("Eligible Students:")
  for student in eligible_students:
    print(student)

# Get the number of students
n = int(input("Enter the number of students: "))
process_applications(n)
