# Write a program to compute sin x for given x. The user should supply x and a positive integer n. We compute the sine of x using the series and the computation should use all terms in the series up through the term involving xn sin x = x - x3/3! + x5/5! - x7/7! + x9/9! ........

def factorial(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

def sin_x(x, n):
    sin_x_value = 0.0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
        sin_x_value += term
    return sin_x_value

x = float(input("Enter the value of x in radians: "))
n = int(input("Enter the number of terms n: "))

sin_x_value = sin_x(x, n)
print(f"The value of sin ({x}) using {n} terms is: {sin_x_value}")
