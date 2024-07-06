'''
Write a function to compute the sum of digits of each number of a given list.
'''

def sum_of_digits(lst):
    return sum([sum([int(i) for i in str(j) if i.isdigit()]) for j in lst])


assert sum_of_digits([10,2,56])==14
assert sum_of_digits([[10,20,4,5,'b',70,'a']])==19
assert sum_of_digits([10,20,-4,5,-70])==19
