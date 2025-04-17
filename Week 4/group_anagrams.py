# Group all strings that are anagrams of each other into seperate lists.
# Two strings are anagrams if they contain the same characters in a different order.

def group_anagrams(words):
    sorted_values = {}
    
    for word in words:
        new_word = "".join(sorted(word))
        if new_word not in sorted_values:
            sorted_values[new_word] = [word]
        else:
            sorted_values[new_word].append(word)
            
    return list(sorted_values.values())
        
words = ["bat", "tab", "tap", "pat", "cat", "act"]
print(group_anagrams(words=words))