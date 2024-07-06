'''
Write a python function to check whether the given strings are rotations of each other or not.
'''

def are_Rotations(str1, str2):
    if len(str1) != len(str2):
        return False
    temp = str1 + str1
    if temp.count(str2) > 0:
        return True
    return False


assert are_Rotations("abc","cba") == False
assert are_Rotations("abcd","cdba") == False
assert are_Rotations("abacd","cdaba") == True
