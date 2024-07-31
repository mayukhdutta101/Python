#Write a program which finds out whether a given name is present in a list or not

names = ["Harry", "Mayukh", "Rick", "Shuvam", "Bob", "Anna"]

search = input("Enter the name you want to search: ")
if(search in names):
    print("Name present in the list")
else:
    print("Name not present in the list")