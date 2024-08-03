# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, _solve_quadratic_eqn_.

import math

def solve_quadratic_eqn_(a, b, c):
    if a == 0:
        if b == 0:
            return "No solution" if c != 0 else "Infinite solutions"
        return [-c / b]
    
    discriminant = b ** 2 - 4 * a * c
    
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return [root1, root2]
    elif discriminant == 0:
        root = -b / (2 * a)
        return [root]
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return [root1, root2]


print("Quadratic Equation Solver: ax² + bx + c = 0")
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
solutions = solve_quadratic_eqn_(a, b, c)
if isinstance(solutions, str):
    print(solutions)
else:
    for i, solution in enumerate(solutions, start=1):
        print(f"Solution {i}: {solution}")

