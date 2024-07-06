'''
Write a function to iterate over elements repeating each as many times as its count.
'''

def count_variable(p, q, r, s):
    return ['p']*p + ['q']*q + ['r']*r + ['s']*s


assert count_variable(4,2,0,-2)==['p', 'p', 'p', 'p', 'q', 'q'] 
assert count_variable(0,1,2,3)==['q', 'r', 'r', 's', 's', 's'] 
assert count_variable(11,15,12,23)==['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's']
