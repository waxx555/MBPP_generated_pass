'''
Write a function to find the largest palindromic number in the given array.
'''

def largest_palindrome(arr, n):
    arr.sort()
    for i in range(n-1, -1, -1):
        if str(arr[i]) == str(arr[i])[::-1]:
            return arr[i]
    return -1


assert largest_palindrome([1, 232, 54545, 999991], 4) == 54545
assert largest_palindrome([1, 2, 3, 4, 5, 50], 6) == 5
assert largest_palindrome([1, 3, 7, 9, 45], 5)  == 9
