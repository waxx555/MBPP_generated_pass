'''
Write a function to reflect the run-length encoding from a list.
'''

def encode_list(lst):
    result = []
    count = 1
    for i in range(1,len(lst)):
        if lst[i] == lst[i-1]:
            count += 1
        else:
            result.append([count,lst[i-1]])
            count = 1
    result.append([count,lst[-1]])
    return result


assert encode_list([1,1,2,3,4,4.3,5,1])==[[2, 1], [1, 2], [1, 3], [1, 4], [1, 4.3], [1, 5], [1, 1]]
assert encode_list('automatically')==[[1, 'a'], [1, 'u'], [1, 't'], [1, 'o'], [1, 'm'], [1, 'a'], [1, 't'], [1, 'i'], [1, 'c'], [1, 'a'], [2, 'l'], [1, 'y']]
assert encode_list('python')==[[1, 'p'], [1, 'y'], [1, 't'], [1, 'h'], [1, 'o'], [1, 'n']]
