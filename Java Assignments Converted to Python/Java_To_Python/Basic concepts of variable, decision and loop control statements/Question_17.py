'''
Write a program to print the following pattern: 
1      1
 2    2
  3  3
    4
'''

def print_pattern(rows):
    for i in range(1, rows + 1):
        print(' ' * (i - 1), end='')
        print(i, end='')
        if i != rows:
            spaces = 2 * (rows - i) - 1
            print(' ' * spaces, end='')
            print(i)
        else:
            print()  

rows = int(input("Enter the number of rows: "))
print_pattern(rows)
