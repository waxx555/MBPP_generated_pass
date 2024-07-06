'''
Write a function to find out the second most repeated (or frequent) string in the given sequence.
'''

def second_frequent(lst):
    freq = {}
    for i in lst:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return freq[1][0]


assert second_frequent(['aaa','bbb','ccc','bbb','aaa','aaa']) == 'bbb'
assert second_frequent(['abc','bcd','abc','bcd','bcd','bcd']) == 'abc'
assert second_frequent(['cdma','gsm','hspa','gsm','cdma','cdma']) == 'gsm'
