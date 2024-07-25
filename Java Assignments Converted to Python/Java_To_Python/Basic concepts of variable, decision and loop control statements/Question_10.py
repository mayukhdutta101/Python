# Write a program to convert a Binary Number to Decimal and Decimal to Binary

def binary_to_decimal(binary_str):

    try:
        decimal_number = int(binary_str, 2)
        return decimal_number
    except ValueError:
        print("Invalid binary number.")
        return None

def decimal_to_binary(decimal_int):

    if decimal_int < 0:
        print("Please enter a non-negative integer.")
        return None
    binary_str = bin(decimal_int)[2:]
    return binary_str

if __name__ == "__main__":
    binary_number = "1010"
    decimal_result = binary_to_decimal(binary_number)
    print(f"Binary {binary_number} is decimal {decimal_result}")

    decimal_number = 10
    binary_result = decimal_to_binary(decimal_number)
    print(f"Decimal {decimal_number} is binary {binary_result}")

