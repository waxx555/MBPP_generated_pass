'''
Write a function to find frequency of the elements in a given list of lists using collections module.
'''

from collections import Counter
def freq_element(arr):
    return dict(Counter([i for j in arr for i in j]))




assert freq_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]])==({2: 3, 1: 2, 5: 2, 3: 1, 4: 1, 6: 1, 7: 1, 9: 1})
assert freq_element([[1,2,3,4],[5,6,7,8],[9,10,11,12]])==({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1})
assert freq_element([[15,20,30,40],[80,90,100,110],[30,30,80,90]])==({30: 3, 80: 2, 90: 2, 15: 1, 20: 1, 40: 1, 100: 1, 110: 1})
