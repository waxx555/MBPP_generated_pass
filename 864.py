'''
Write a function to find palindromes in a given list of strings using lambda function.
'''

palindrome_lambda = lambda lst: [i for i in lst if i==i[::-1]]



assert palindrome_lambda(["php", "res", "Python", "abcd", "Java", "aaa"])==['php', 'aaa']
assert palindrome_lambda(["abcd", "Python", "abba", "aba"])==['abba', 'aba']
assert palindrome_lambda(["abcd", "abbccbba", "abba", "aba"])==['abbccbba', 'abba', 'aba']
