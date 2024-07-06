'''
Write a function to find the next smallest palindrome of a specified number.
'''

def next_smallest_palindrome(n):
    n+=1
    while str(n)!=str(n)[::-1]:
        n+=1
    return n


assert next_smallest_palindrome(99)==101
assert next_smallest_palindrome(1221)==1331
assert next_smallest_palindrome(120)==121
