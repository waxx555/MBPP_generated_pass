'''
Write a python function to find the first maximum length of even word.
'''

def find_Max_Len_Even(s):
    s = s.split()
    max_len = -1
    for word in s:
        if len(word) % 2 == 0 and len(word) > max_len:
            max_len = len(word)
            max_word = word
    if max_len == -1:
        return "-1"
    return max_word


assert find_Max_Len_Even("python language") == "language"
assert find_Max_Len_Even("maximum even length") == "length"
assert find_Max_Len_Even("eve") == "-1"
