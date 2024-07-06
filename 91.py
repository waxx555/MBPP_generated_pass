'''
Write a function to check if a substring is present in a given list of string values.
'''

def find_substring(arr, sub):
    for i in arr:
        if sub in i:
            return True
    return False


assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
assert find_substring(["red", "black", "white", "green", "orange"],"abc")==False
assert find_substring(["red", "black", "white", "green", "orange"],"ange")==True
