'''
Print the pattern upto N lines:
1 2 
4 3               N=2

1 2 3
8 9 4
7 6 5           N=3

1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7        N=4

'''

def print_pattern(n):
    matrix = [[0] * n for _ in range(n)]
    start= 0
    end = n
    num = 1

    while start < end:
        for i in range(start, end):
            matrix[start][i] = num
            num += 1
        for i in range(start + 1, end):
            matrix[i][end - 1] = num
            num += 1
        for i in range(end - 2, start - 1, -1):
            matrix[end - 1][i] = num
            num += 1
        for i in range(end - 2, start, -1):
            matrix[i][start] = num
            num += 1
        start += 1
        end -= 1

    for row in matrix:
        print(" ".join(str(x) for x in row))

n = int(input("Enter the number of terms: "))
print_pattern(n)
