'''
Create fruits, vegetables and animal products tuples. 

I.Join the three tuples and assign it to a variable called food_stuff_tp.
II.Change the about food_stuff_tp  tuple to a food_stuff_lt list
III.Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
IV.Slice out the first three items and the last three items from food_staff_lt list
V.Delete the food_staff_tp tuple completely
'''

fruits = ('apple','mango','guava','banana','strawberry','avocado')
vegetables = ('potato','onion','pumpkin','carrot','tomato','papaya')
animals = ('lion','leopard','cow','zebra','dog','cat')

# I.Join the three tuples and assign it to a variable called food_stuff_tp.
food_stuff_tp = fruits + vegetables + animals
print(food_stuff_tp)

# II.Change the about food_stuff_tp  tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# III.Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
length = len(food_stuff_tp)
mid_index = length//2
if length % 2 == 0:
    middle_item = food_stuff_tp[mid_index - 1:mid_index + 1]
else:
    middle_item = food_stuff_tp[mid_index]

print(middle_item)

# IV.Slice out the first three items and the last three items from food_staff_lt list
f_three = food_stuff_tp[:3]
l_three = food_stuff_tp[-3:]
print(f_three)
print(l_three)

# V.Delete the food_staff_tp tuple completely
del food_stuff_tp
try:
    print(food_stuff_tp)
except NameError:
    print("'food_stuff_tp' has been deleted.")