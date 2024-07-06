'''
Write a python function to check whether a sequence of numbers has an increasing trend or not.
'''

def increasing_trend(lst):
    return lst == sorted(lst)


assert increasing_trend([1,2,3,4]) == True
assert increasing_trend([4,3,2,1]) == False
assert increasing_trend([0,1,4,9]) == True
