# Count frequencies of elements using hashing
array = [1, 4, 5, 2, 6, 1, 7, 3, 4, 2, 6, 2, 1, 1, 3, 2]

def count_freq(arr):
    frequency = {}
    
    for element in arr:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
            
    return frequency

print(count_freq(array))