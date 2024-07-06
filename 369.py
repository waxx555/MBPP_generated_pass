'''
Write a function to find the lateral surface area of cuboid
'''

def lateralsurface_cuboid(l,b,h):
    return 2*h*(l+b)


assert lateralsurface_cuboid(8,5,6)==156
assert lateralsurface_cuboid(7,9,10)==320
assert lateralsurface_cuboid(10,20,30)==1800
