'''
Write a function to decode a run-length encoded given list.
'''

def decode_list(lst):
    result = []
    for i in lst:
        if type(i) == list:
            result.extend([i[1]]*i[0])
        else:
            result.append(i)
    return result


assert decode_list([[2, 1], 2, 3, [2, 4], 5,1])==[1,1,2,3,4,4,5,1]
assert decode_list(['a', 'u', 't', 'o', 'm', 'a', 't', 'i', 'c', 'a', [2, 'l'], 'y'])==['a', 'u', 't', 'o', 'm', 'a', 't', 'i', 'c', 'a', 'l', 'l', 'y']
assert decode_list(['p', 'y', 't', 'h', 'o', 'n'])==['p', 'y', 't', 'h', 'o', 'n']
