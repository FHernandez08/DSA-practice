def most_frequent(arr):
    frequency = {}
    max_freq = 0
    most_frequent_element = None
    
    for num in arr:
        if num in frequency:
            frequency[num] += 1
            if frequency[num] > max_freq:
                max_freq = frequency[num]
                most_frequent_element = num
        else:
            frequency[num] = 1
            
    return most_frequent_element

nums = [1, 3, 2, 3, 4, 1, 1]
print(most_frequent(nums))