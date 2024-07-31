'''
Write a program to find out whether a student has passed or failed if it requires a 
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
take marks as an input from the user.
'''

print("Total marks: 100")
m1 = int(input("Enter the marks of first subject: "))
m2 = int(input("Enter the marks of second subject: "))
m3 = int(input("Enter the marks of third subject: "))

#check for total percentage

total_percentage = (100*(m1+m2+m3))/300

if(total_percentage>=40 and m1>33 and m2>33 and m3>33):
    print("PASS!!!")
else:
    print("FAIL :(")

