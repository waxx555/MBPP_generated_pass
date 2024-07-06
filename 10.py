'''
Write a function to get the n smallest items from a dataset.
'''

def small_nnum(arr,n):
    arr.sort()
    return arr[:n]



assert small_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2)==[10,20]
assert small_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],5)==[10,20,20,40,50]
assert small_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],3)==[10,20,20]
