#Write a program to find out whether a given post is talking about “Mayukh” or not

post = input("Enter the post: \n")

if("Mayukh".lower() in post.lower()):
    print("The post is talking about Mayukh")
else:
    print("The post is not talking about Mayukh")