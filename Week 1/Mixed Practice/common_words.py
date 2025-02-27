# Common Words in Two Dictionaries (Dictionaries & Sets)
# You are given two dictionaries (dict1 & dict2), where the keys are words, and the values represent their frequencies.
# Write a function to return a set of words that appear in both dictionaries at least once.

def common_dict(dict_1, dict_2):
    return set(dict_1.keys()) & set(dict_2.keys())

dict1 = {"apple": 3, "banana": 5, "cherry": 2, "date": 1}
dict2 = {"banana": 4, "cherry": 1, "fig": 2, "grape": 3}

print(common_dict(dict1, dict2))