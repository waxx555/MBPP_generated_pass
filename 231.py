'''
Write a function to find the maximum sum in the given right triangle of numbers.
'''

def max_sum(triangle, n):
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]


assert max_sum([[1], [2,1], [3,3,2]], 3) == 6
assert max_sum([[1], [1, 2], [4, 1, 12]], 3) == 15 
assert max_sum([[2], [3,2], [13,23,12]], 3) == 28
