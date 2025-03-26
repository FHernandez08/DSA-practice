# Count frequencies of elements using hashing
def count_frequency(arr):
    frequency_dict = {}
    
    for item in arr:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
            
    return frequency_dict

array = [1, 2, 3, 3, 4, 4, 1, 5, 6, 5, 4, 2, 1, 4]
print(count_frequency(arr=array))