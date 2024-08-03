# Compute the sum up to n terms in the series 1 - 1/2 + 1/3 - 1/4 + 1/5 -... 1/n where n is a positive integer and input by user.

def compute_sum(r):
    total_sum = 0.0
    for i in range(1, r+1):
        if(i%2 == 0):
            total_sum -= 1/i
        else:
            total_sum += 1/i
    return total_sum

r = int(input("Enter the range: "))

compute = compute_sum(r)
print(f"Series upta {r} terms is: {compute}")