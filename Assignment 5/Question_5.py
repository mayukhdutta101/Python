'''
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

From the above sets A and B
I.Join A and B
II.Find A intersection B
III.Is A subset of B
IV.Are A and B disjoint sets
V.Join A with B and B with A
VI.What is the symmetric difference between A and B
VII.Delete the sets completely
'''

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# I.Join A and B
joined_set = A.union(B)
print(f"Joined Set: {joined_set}")

# II.Find A intersection B
instersection_set = A.intersection(B)
print(f"After intersection: {instersection_set}")

# III.Is A subset of B
is_subset = A.issubset(B)
print(F"Subset: {is_subset}")

# IV.Are A and B disjoint sets
is_disjoint_set = A.isdisjoint(B)
print(f"Is disjoint: {is_disjoint_set}")

# V.Join A with B and B with A
joined_set_A_B = A.union(B)
print(f"Joined Set A with B: {joined_set_A_B}")
joined_set_B_A = B.union(A)
print(f"Joined Set B with A: {joined_set_B_A}")

# VI.What is the symmetric difference between A and B
symm_diff = A.symmetric_difference(B)
print(f"Symmetric difference: {symm_diff}")

# VII.Delete the sets completely
del A,B
try:
    print(A,B)
except NameError:
    print("Sets A and B are deleted.")