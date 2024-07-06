'''
Write a function to find modulo division of two lists using map and lambda function.
'''

def moddiv_list(a,b):
    return list(map(lambda x,y: x%y,a,b))


assert moddiv_list([4,5,6],[1, 2, 3])==[0, 1, 0]
assert moddiv_list([3,2],[1,4])==[0, 2]
assert moddiv_list([90,120],[50,70])==[40, 50]
