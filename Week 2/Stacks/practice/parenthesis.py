def parenthesis(curr_item):
    opening_item = []
    
    for item in curr_item:
        if item in "({[":
            opening_item.append(item)
        else:
            if not opening_item:
                return False
            else:
                top_item = opening_item.pop()
                if item == ')' and top_item != '(':
                    return False
                elif item == '}' and top_item != '{':
                    return False
                elif item == ']' and top_item != '[':
                    return False
    return len(opening_item) == 0


#### TEST CASES ####
# Valid cases
print(parenthesis("()"))  # True
print(parenthesis("({[]})"))  # True
print(parenthesis("{[()]}"))  # True

# Invalid cases
print(parenthesis("({[})"))  # False
print(parenthesis("((())"))  # False
print(parenthesis("{[()]}]"))  # False
print(parenthesis("]"))  # False
