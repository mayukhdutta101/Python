'''
Write a python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
'''

def print_table(n):
    for i in range(1,n+1):
        print(i,end=' ')
        for j in range(4):
            print(i**j,end=' ')
        print()

n = int(input("Enter the number of terms: "))
print_table(n)