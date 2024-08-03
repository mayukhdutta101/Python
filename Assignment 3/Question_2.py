# Write a function called calculate_slope which return the slope of a linear equation

def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
        return "Undefined"
    return (y2 - y1) / (x2 - x1)

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
slope = calculate_slope(x1, y1, x2, y2)
print(f"The slope of the line between ({x1}, {y1}) and ({x2}, {y2}) is {slope}")
