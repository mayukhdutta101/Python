'''
Write program for the patterns given bellow:
1
2 3 4
5 6 7 8 9
'''

n = int(input("Enter the number of rows: "))

num=1
for i in range(1, n+1):
    for j in range(i):
        print(num, end=' ')
        num += 1
    print()