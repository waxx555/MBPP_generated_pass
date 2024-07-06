'''
Write a function to abbreviate 'road' as 'rd.' in a given string.
'''

import re

def road_rd(s):
    return re.sub(r'\bRoad\b', 'Rd.', s)


assert road_rd("ravipadu Road")==('ravipadu Rd.')
assert road_rd("palnadu Road")==('palnadu Rd.')
assert road_rd("eshwar enclave Road")==('eshwar enclave Rd.')
