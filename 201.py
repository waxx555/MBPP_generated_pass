'''
Write a python function to check whether the elements in a list are same or not.
'''

def chkList(lst):
    return all(i == lst[0] for i in lst)


assert chkList(['one','one','one']) == True
assert chkList(['one','Two','Three']) == False
assert chkList(['bigdata','python','Django']) == False
