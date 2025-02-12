# Sets Operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

#  -Union-
union_set = set1.union(set2)
# print(union_set)

#  -Intersection-
intersection = set1.intersection(set2)
# print(intersection)

#  -Difference-
diff_set = set1.difference(set2)
# print(diff_set)

#  -Symmetric Difference-
symm_diff_set = set1.symmetric_difference(set2)
# print(symm_diff_set)

#  -Subset and Superset-
is_subset = set2.issubset(set1)
is_superset = set1.issuperset(set2)

#  -Adding and Removing-
my_set = {1, 2, 3, 4}
print(my_set)

my_set.add(5)
my_set.remove(2)

print(my_set)