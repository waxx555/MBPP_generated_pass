'''
Write a function to check whether the given key is present in the dictionary or not.
'''

def is_key_present(d, k):
    return k in d


assert is_key_present({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60},5)==True
assert is_key_present({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60},6)==True
assert is_key_present({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60},10)==False
