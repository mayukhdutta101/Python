'''
The following is a list of 10 students ages:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

I.Sort the list and find the min and max age
II.Add the min age and the max age again to the list
III.Find the median age (one middle item or two middle items divided by two)
IV.Find the average age (sum of all items divided by their number )
V.Find the range of the ages (max minus min)
VI.Compare the value of (min - average) and (max - average), use _abs()_ method
'''

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# I. Sort the list and find the min and max age
sorted_ages = sorted(ages)
min_age = sorted_ages[0]
max_age = sorted_ages[-1]

# II. Add min age and max age again to the list
ages_with_extremes = ages + [min_age, max_age]

# III. Find the median age
def median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

median_age = median(ages_with_extremes)

# IV. Find the average age
def average(lst):
    return sum(lst) / len(lst)

average_age = average(ages_with_extremes)

# V. Find the range of the ages
range_age = max_age - min_age

# VI. Compare (min - average) and (max - average) using abs()
min_minus_avg = abs(min_age - average_age)
max_minus_avg = abs(max_age - average_age)

print(f"{sorted_ages} \n{min_age} \n{max_age} \n{ages_with_extremes} \n{median_age} \n{average_age} \n{range_age} \n{min_minus_avg} \n{max_minus_avg}")

