'''
Print the pattern upto N Lines: 
  .
 /_\   N=2
  .
 / \ 
/___\   N=3
   .
  / \ 
 /   \ 
/_____\   N=4

'''

def print_triangle(n):
    print(" " * n + ".")

    for i in range(1, n):
        print(" " * (n - i - 1), end="")
        print(" /" + " " * (2 * i - 1) + "\\")
    print("/" + "_" * (2 * n - 1) + "\\")

n = int(input("Enter the value of N: "))
print_triangle(n)