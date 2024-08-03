"""
Print a number as a 8 segment display N Lines: 
 _
 _|     N=2
 |_
 _
 _|
 _|     N=3

 |_|
 |      N=4
"""

def print_digit(digit):
    segments = [
        " _ \n| |\n|_|",  # 0
        "   \n  |\n  |",  # 1
        " _ \n |\n| ",    # 2
        " _ \n _|\n _|",  # 3
        "   \n|_|\n  |",  # 4
        " _ \n|_ \n _|",  # 5
        " _ \n|_ \n|_|",  # 6
        " _ \n  |\n  |",  # 7
        " _ \n||\n||",    # 8
        " _ \n|_|\n _|"   # 9
    ]
    return segments[digit]

def print_number_as_segment_display(N):
    number_str = str(N)
    lines = ["", "", ""]
    for digit_char in number_str:
        digit = int(digit_char)
        segment_lines = print_digit(digit).split('\n')
        for i in range(3):
            lines[i] += segment_lines[i] + " "

    for line in lines:
        print(line)

N = int(input("Enter the number N: "))
print_number_as_segment_display(N)