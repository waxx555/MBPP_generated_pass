'''
Write a function to generate a square matrix filled with elements from 1 to n raised to the power of 2 in spiral order.
'''

def generate_matrix(n):
    matrix = [[0]*n for i in range(n)]
    i, j, di, dj = 0, 0, 0, 1
    for k in range(1, n*n+1):
        matrix[i][j] = k
        if matrix[(i+di)%n][(j+dj)%n]:
            di, dj = dj, -di
        i += di
        j += dj
    return matrix


assert generate_matrix(3)==[[1, 2, 3], [8, 9, 4], [7, 6, 5]] 
assert generate_matrix(2)==[[1,2],[4,3]]
assert generate_matrix(7)==[[1, 2, 3, 4, 5, 6, 7], [24, 25, 26, 27, 28, 29, 8], [23, 40, 41, 42, 43, 30, 9], [22, 39, 48, 49, 44, 31, 10], [21, 38, 47, 46, 45, 32, 11], [20, 37, 36, 35, 34, 33, 12], [19, 18, 17, 16, 15, 14, 13]]
