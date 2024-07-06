'''
Write a function to verify validity of a string of parentheses.
'''

def is_valid_parenthese(s):
    stack = []
    mapping = {')':'(', '}':'{', ']':'['}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack


assert is_valid_parenthese("(){}[]")==True
assert is_valid_parenthese("()[{)}")==False
assert is_valid_parenthese("()")==True
