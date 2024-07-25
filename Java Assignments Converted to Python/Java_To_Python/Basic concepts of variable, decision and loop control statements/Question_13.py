# Write a program to generate all combination of 1, 2, or 3 using loop.

def list_combination():
    combinations = []
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                combinations.append(str(i)+str(j)+str(k))
    return combinations

print(list_combination())