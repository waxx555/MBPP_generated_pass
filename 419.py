'''
Write a function to round every number of a given list of numbers and print the total sum multiplied by the length of the list.
'''

def round_and_sum(lst):
    return sum([round(i) for i in lst])*len(lst)



assert round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])==243
assert round_and_sum([5,2,9,24.3,29])==345
assert round_and_sum([25.0,56.7,89.2])==513
