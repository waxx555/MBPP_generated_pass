'''
Write a function to check whether all items of a list are equal to a given string.
'''

def check_element(lst,element):
    return all(i==element for i in lst)


assert check_element(["green", "orange", "black", "white"],'blue')==False
assert check_element([1,2,3,4],7)==False
assert check_element(["green", "green", "green", "green"],'green')==True
