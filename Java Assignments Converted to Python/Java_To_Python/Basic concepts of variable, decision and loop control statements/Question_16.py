'''
Write a program to print the following pattern: 
     1
   2 1 2
 3 2 1 2 3
4 3 2 1 2 3 4
'''

rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
  # Print spaces
  for j in range(rows - i):
    print(" ", end=" ")
  # Print numbers
  for j in range(i, 0, -1):
    print(j, end=" ")
  for j in range(2, i + 1):
    print(j, end=" ")
  print()
