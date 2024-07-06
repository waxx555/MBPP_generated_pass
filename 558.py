'''
Write a python function to find the digit distance between two integers.
'''

def digit_distance_nums(num1,num2):
    return sum([int(i) for i in str(abs(num1-num2))])


assert digit_distance_nums(1,2) == 1
assert digit_distance_nums(23,56) == 6
assert digit_distance_nums(123,256) == 7
