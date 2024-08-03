# Write a program to compute cosine of x. The user should supply x and a positive integer n. We compute the cosine of x using the series and the computation should use all terms in the series up through the term involving xn cos x = 1 - x2/2! + x4/4! - x6/6! ....

def factorial(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

def cos_x(x, n):
    cos_x_value = 0.0
    for i in range(n + 1):
        term = ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
        cos_x_value += term
    return cos_x_value

x = float(input("Enter the value of x in radians: "))
n = int(input("Enter the number of terms n: "))

cos_x_value = cos_x(x, n)
print(f"The value of cos({x}) using {n} terms is: {cos_x_value}")
