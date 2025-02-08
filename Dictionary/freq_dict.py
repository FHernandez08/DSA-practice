# calcualate the frequency of a word w/ dictionary

list_dict = ['Lakers', 'Astros', 'Dodgers', 'Blue Jays', 'Blue Jays', 'Astros', 
             'Dodgers', 'Blue Jays', 'Mavericks']

list_words = {}

for item in list_dict:
    list_words[item] = list_words.get(item, 0) + 1

print(list_words)