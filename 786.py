'''
Write a function to locate the right insertion point for a specified value in sorted order.
'''

def right_insertion(lst, val):
    for i in range(len(lst)):
        if lst[i]>=val:
            return i
    return len(lst)


assert right_insertion([1,2,4,5],6)==4
assert right_insertion([1,2,4,5],3)==2
assert right_insertion([1,2,4,5],7)==4
