# Group anagrams using a dictionary
from collections import defaultdict

def group_anagrams(arr):
    frequency = defaultdict(list)
    
    for word in arr:
        sorted_word = "".join(sorted(word))
        frequency[sorted_word].append(word)
        
    return list(frequency.values())
    
    