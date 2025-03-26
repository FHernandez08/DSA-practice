# Solve a word frequency problem
def word_frequency(string):
    frequency = {}
    
    for word in string:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
            
    return frequency

string_use = "hello"
print(word_frequency(string=string_use))