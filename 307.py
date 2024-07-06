'''
Write a function to get a colon of a tuple.
'''

def colon_tuplex(tup, index, value):
    lst = list(tup)
    lst[index].append(value)
    return tuple(lst)



assert colon_tuplex(("HELLO", 5, [], True) ,2,50)==("HELLO", 5, [50], True) 
assert colon_tuplex(("HELLO", 5, [], True) ,2,100)==(("HELLO", 5, [100],True))
assert colon_tuplex(("HELLO", 5, [], True) ,2,500)==("HELLO", 5, [500], True)
