'''
Write a python function to find number of elements with odd factors in a given range.
'''

def count_Odd_Squares(a,b):
    count = 0
    for i in range(a,b+1):
        if int(i**0.5)**2 == i:
            count += 1
    return count


assert count_Odd_Squares(5,100) == 8
assert count_Odd_Squares(8,65) == 6
assert count_Odd_Squares(2,5) == 1
