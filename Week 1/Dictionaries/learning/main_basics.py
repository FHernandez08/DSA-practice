# Comprehension
squares = {x: x ** 2 for x in range(1, 6)}
print(squares)

my_dict = {'a': 1, 'b': 2, 'c': 3}

# accessing keys, values, items
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

# getting value from a key
print(my_dict.get('b'))

# removes the pair from the dictionary
my_dict.pop('b')
print(my_dict)

# adds specific pair to the dictionary
my_dict.update({'d': 4})
print(my_dict)

my_dict.clear()
print(my_dict)
