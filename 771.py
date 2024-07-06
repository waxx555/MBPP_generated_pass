'''
Write a function to check if the given expression is balanced or not.
'''

def check_expression(exp):
    stack = []
    for i in exp:
        if i in ['{', '(', '[']:
            stack.append(i)
        else:
            if not stack:
                return False
            if i == '}' and stack[-1] == '{':
                stack.pop()
            elif i == ')' and stack[-1] == '(':
                stack.pop()
            elif i == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False
    return len(stack) == 0


assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{]") == False
assert check_expression("{()}[{}][]({})") == True
