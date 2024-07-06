'''
Write a function to count the elements in a list until an element is a tuple.
'''

def count_elim(lst):
    count = 0
    for i in lst:
        if isinstance(i, tuple):
            break
        count += 1
    return count


assert count_elim([10,20,30,(10,20),40])==3
assert count_elim([10,(20,30),(10,20),40])==1
assert count_elim([(10,(20,30,(10,20),40))])==0
