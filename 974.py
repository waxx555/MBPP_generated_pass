'''
Write a function to find the minimum total path sum in the given triangle.
'''

def min_sum_path(triangle):
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
    return triangle[0][0]


assert min_sum_path([[ 2 ], [3, 9 ], [1, 6, 7 ]]) == 6
assert min_sum_path([[ 2 ], [3, 7 ], [8, 5, 6 ]]) == 10 
assert min_sum_path([[ 3 ], [6, 4 ], [5, 2, 7 ]]) == 9
