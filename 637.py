'''
Write a function to check whether the given amount has no profit and no loss
'''

def noprofit_noloss(cp,sp):
    return cp==sp


assert noprofit_noloss(1500,1200)==False
assert noprofit_noloss(100,100)==True
assert noprofit_noloss(2000,5000)==False
