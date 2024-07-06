'''
Write a function to find the item with maximum frequency in a given list.
'''

def max_occurrences(lst):
    freq = {}
    for i in lst:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    max_freq = max(freq.values())
    for key, value in freq.items():
        if value == max_freq:
            return key, value
    return None


assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==(2, 5)
assert max_occurrences([2,3,8,4,7,9,8,7,9,15,14,10,12,13,16,16,18])==(8, 2)
assert max_occurrences([10,20,20,30,40,90,80,50,30,20,50,10])==(20, 3)
