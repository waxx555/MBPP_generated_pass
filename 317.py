'''
Write a function to reflect the modified run-length encoding from a list.
'''

def modified_encode(lst):
    result = []
    count = 1
    for i in range(1,len(lst)):
        if lst[i] == lst[i-1]:
            count += 1
        else:
            if count == 1:
                result.append(lst[i-1])
            else:
                result.append([count,lst[i-1]])
            count = 1
    if count == 1:
        result.append(lst[-1])
    else:
        result.append([count,lst[-1]])
    return result


assert modified_encode([1,1,2,3,4,4,5,1])==[[2, 1], 2, 3, [2, 4], 5, 1]
assert modified_encode('automatically')==['a', 'u', 't', 'o', 'm', 'a', 't', 'i', 'c', 'a', [2, 'l'], 'y']
assert modified_encode('python')==['p', 'y', 't', 'h', 'o', 'n']
