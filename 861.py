'''
Write a function to find all anagrams of a string in a given list of strings using lambda function.
'''

anagram_lambda = lambda lst, s: [i for i in lst if sorted(i)==sorted(s)]


assert anagram_lambda(["bcda", "abce", "cbda", "cbea", "adcb"],"abcd")==['bcda', 'cbda', 'adcb']
assert anagram_lambda(["recitals"," python"], "articles" )==["recitals"]
assert anagram_lambda([" keep"," abcdef"," xyz"]," peek")==[" keep"]
