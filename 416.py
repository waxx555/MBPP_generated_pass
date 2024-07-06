'''
Write a function to find the maximum sum we can make by dividing number in three parts recursively and summing them up together for the given number.
'''

def breakSum(n):
    if n == 0:
        return 0
    return max(n, breakSum(n//2) + breakSum(n//3) + breakSum(n//4))


assert breakSum(12) == 13
assert breakSum(24) == 27
assert breakSum(23) == 23
