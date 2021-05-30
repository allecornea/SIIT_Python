# Create two sets with 10 numbers each (some of the numbers should be present in both sets). With these two sets,
# exemplify the following basic sets operations: union, intersection, difference and symmetric difference.

first_set = {11, 5, 9, 19, 23, 20, 8, 4, 12, 30}
second_set = {31, 2, 67, 57, 33, 20, 18, 4, 9, 11}

union_set = first_set.union(second_set)
print(union_set)

intersection_set = first_set.intersection(second_set)
print(intersection_set)

first_difference_set = first_set.difference(second_set)
second_difference_set = second_set.difference(first_set)

print(first_difference_set)
print(second_difference_set)

symmetric_difference_set = first_set.symmetric_difference(second_set)
print(symmetric_difference_set)
