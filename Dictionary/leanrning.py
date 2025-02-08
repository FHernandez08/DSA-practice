from collections import defaultdict

# Dictionary Comprehension
squares = {x: x ** 2 for x in range(1, 6)}
print(squares)

# Dictionary Methods
#  -keys()-
print(squares.keys())

#  -values()-
print(squares.values())

#  -items()-
print(squares.items())

#  -get()-
print(squares.get(2))

#  -pop()-
print(squares.pop(3))
print(squares)

# Nested Dictionaries
student_scores = {
    'John': {'math': 90, 'science': 85},
    'Alice': {'math': 95, 'science': 88}
}

print(student_scores)
print(student_scores['Alice']['math'])

# Sorting
scores = {'John': 90, 'Alice': 95, 'Bob': 88}

sorted_by_keys = {k: scores[k] for k in sorted(scores)}
print(sorted_by_keys)

sorted_by_values = {k: v for k, v in sorted(scores.items(), key=lambda item: item[1])}
print(sorted_by_values)

# handling missing keys
my_dict = {'a': 1, 'b': 2}

#  -setdefault()-
my_dict.setdefault('c', 3)
print(my_dict)

#  -defaultdict-
defaultdict = defaultdict(int)
print(defaultdict['a'])

#  -get() w/ default value-
print(my_dict.get('d', 'Not Found'))