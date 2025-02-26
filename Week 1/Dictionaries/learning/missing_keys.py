# Handling Missing Keys
my_dict = {'a': 1, 'b': 2}

# Using setdefault() to provide a default value
my_dict.setdefault('c', 3)
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

# Using defaultdict to provide a default value factory
from collections import defaultdict
default_dict = defaultdict(int)
print(default_dict['a'])  # Output: 0

# Using get() method with a default value
print(my_dict.get('d', 'Not found'))  # Output: Not found