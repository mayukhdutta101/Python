# Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

string = input("Enter a string: ")
if(string.upper() == "YES"):
    print("yes")
else:
    print("no")
