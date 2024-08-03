# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

def reverse_list(array):
    reversed_array = []
    for i in range(len(array) - 1, -1, -1):
        reversed_array.append(array[i])
    return reversed_array

array = [None] * 5
for i in range(len(array)):
    array[i] = int(input("Enter element in the array: "))
reversed_array = reverse_list(array)
print("Reversed array: ",reversed_array)

