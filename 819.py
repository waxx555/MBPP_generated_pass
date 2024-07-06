'''
Write a function to count the frequency of consecutive duplicate elements in a given list of numbers.
'''

def count_duplic(lst):
    count = 1
    count_lst = []
    num_lst = []
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            count += 1
        else:
            count_lst.append(count)
            num_lst.append(lst[i])
            count = 1
    count_lst.append(count)
    num_lst.append(lst[-1])
    return num_lst, count_lst


assert count_duplic([1,2,2,2,4,4,4,5,5,5,5])==([1, 2, 4, 5], [1, 3, 3, 4])
assert count_duplic([2,2,3,1,2,6,7,9])==([2, 3, 1, 2, 6, 7, 9], [2, 1, 1, 1, 1, 1, 1])
assert count_duplic([2,1,5,6,8,3,4,9,10,11,8,12])==([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
