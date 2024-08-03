#  Declare a function named print_list. It takes a list as a parameter and it prints out each  element of the list

def print_list(elements):
    for element in elements:
        print(element)

list = []
limit = int(input("Enter the number of elements to be present in the list: "))
r=0
while(r<limit):
    list.append(int(input("Enter element in the list: ")))
    r+=1

print_list(list)
