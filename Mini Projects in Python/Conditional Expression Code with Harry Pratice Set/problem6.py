'''
Write a program to calculate the grade of a student from his marks from the 
following scheme:
90 to 100 => Ex
80 to 90 => A
70 to 80 => B
60 to 70 =>C
50 to 60 => D
<50 => F
'''

marks = int(input("Enter the marks: "))

if(marks>90 and marks<=100):
    print("Ex")
elif(marks>80 and marks<=90):
    print("A")
elif(marks>70 and marks<=80):
    print("B")
elif(marks>60 and marks<=70):
    print("C")
elif(marks>=50 and marks<=60):
    print("D")
elif(marks):
    print("F")
else:
    print("Enter valid marks")