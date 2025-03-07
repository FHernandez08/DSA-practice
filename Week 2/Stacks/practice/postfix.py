def postfix(expression):
    stack = []
    
    for item in expression:
        if str(item) not in '+-*/':
            stack.append(item)
        else:
            operand_1 = stack.pop()
            operand_2 = stack.pop()
            if item == '+':
                add_result = operand_1 + operand_2
                stack.append(add_result)
            elif item == '-':
                subtract_result = operand_2 - operand_1
                stack.append(subtract_result)
            elif item == '*':
                multiply_result = operand_1 * operand_2
                stack.append(multiply_result)
            else:
                divide_result = operand_2 // operand_1
                stack.append(divide_result)
                
    return stack.pop()

#### TEST CASES ####
print(postfix([1, 2, '+']))  # Expected output: 3
print(postfix([2, 3, 4, '*', '+']))  # Expected output: 14
print(postfix([5, 3, 2, '/', '-']))  # Expected output: 1