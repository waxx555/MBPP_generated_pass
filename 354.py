'''
Write a function to find t-nth term of arithemetic progression.
'''

def tn_ap(a,n,d):
    return a + (n-1)*d


assert tn_ap(1,5,2)==9
assert tn_ap(2,6,4)==22
assert tn_ap(1,4,5)==16
