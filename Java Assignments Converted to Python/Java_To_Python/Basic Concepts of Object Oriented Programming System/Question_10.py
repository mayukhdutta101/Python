'''
Write a program for following grading system.
Note: 
Percentage>=90% : Grade A
Percentage>=80% : Grade B
Percentage>=70% : Grade C
Percentage>=60% : Grade D
Percentage>=40% : Grade E
Percentage<40% : Grade F
'''

n = int(input("Enter the marks: "))
if(n>100 or n<0):
    print("Enter valid marks.")
else:
    if(n>= 90 and n<=100):
        print("Grade A")
    elif(n>= 80 and n<90):
        print("Grade B")
    elif(n>= 70 and n<80):
        print("Grade C")
    elif(n>= 60 and n<70):
        print("Grade D")
    elif(n>= 40 and n<60):
        print("Grade E")
    elif(n<40):
        print("Grade F")