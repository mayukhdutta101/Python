# Write a program in Python to check if a number is Krishnamurthy number.

def is_krishnamurthy(num):

  copy_num = num
  sum_of_facts = 0

  while copy_num > 0:
    digit = copy_num % 10
    fact = 1
    for i in range(1, digit + 1):
      fact *= i
    sum_of_facts += fact
    copy_num //= 10

  return sum_of_facts == num

num = int(input("Enter a number: "))

if is_krishnamurthy(num):
  print(num, "is a Krishnamurthy number")
else:
  print(num, "is not a Krishnamurthy number")
