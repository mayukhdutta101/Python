# Convert Decimal number to Binary

def decimal_to_binary(num):

  if num == 0:
    return '0'

  binary_str = ''
  while num > 0:
    remainder = num % 2
    binary_str = str(remainder) + binary_str
    num = num // 2

  return binary_str

decimal_num = int(input("Enter a decimal number: "))

print("Binary equivalent:", decimal_to_binary(decimal_num))
