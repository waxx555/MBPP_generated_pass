'''
Write a function to calculate magic square.
'''

def magic_square_test(matrix):
    n = len(matrix)
    sum = 0
    for i in range(n):
        sum += matrix[0][i]
    
    for i in range(n):
        row_sum = 0
        col_sum = 0
        for j in range(n):
            row_sum += matrix[i][j]
            col_sum += matrix[j][i]
        if row_sum != sum or col_sum != sum:
            return False
    
    diag_sum1 = 0
    diag_sum2 = 0
    for i in range(n):
        diag_sum1 += matrix[i][i]
        diag_sum2 += matrix[i][n-i-1]
    
    if diag_sum1 != sum or diag_sum2 != sum:
        return False
    
    return True


assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False
