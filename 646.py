'''
Write a python function to count number of cubes of size k in a cube of size n.
'''

def No_of_cubes(n, k):
    return (n - k + 1) ** 3


assert No_of_cubes(2,1) == 8
assert No_of_cubes(5,2) == 64
assert No_of_cubes(1,1) == 1
