'''
Write a function to find the lateral surface area of a cube.
'''

def lateralsurface_cube(side):
    return 4*side**2


assert lateralsurface_cube(5)==100
assert lateralsurface_cube(9)==324
assert lateralsurface_cube(10)==400
