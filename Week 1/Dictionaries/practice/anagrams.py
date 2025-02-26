def anagram(d1):
    dict = {}
    
    for value in d1:
        key = ''.join(sorted(value))
        
        if key in dict.keys():
            dict[key].append(value)
        else:
            dict[key] = []
            dict[key].append(value)
            
    result = ""
    for key, value in dict.items():
        result = result + ' '.join(value) + ' '
        
    return result

d1 = ['act', 'cat', 'silent', 'listen']
print("Words: ", d1)
print("Anagram: ", anagram(d1))