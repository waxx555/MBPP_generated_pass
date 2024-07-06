'''
Write a python function to find the largest number that can be formed with the given digits.
'''

def find_Max_Num(lst,n):
    lst.sort(reverse = True)
    return int("".join(map(str,lst[:n])))


assert find_Max_Num([1,2,3],3) == 321
assert find_Max_Num([4,5,6,1],4) == 6541
assert find_Max_Num([1,2,3,9],4) == 9321
