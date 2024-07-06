'''
Write a function to remove lowercase substrings from a given string by using regex.
'''

import re

def remove_lowercase(s):
    return re.sub('[a-z]', '', s)


assert remove_lowercase('KDeoALOklOOHserfLoAJSIskdsf') == 'KDALOOOHLAJSI'
assert remove_lowercase('ProducTnamEstreAmIngMediAplAYer') == 'PTEAIMAAY'
assert remove_lowercase('maNufacTuredbYSheZenTechNolOGIes') == 'NTYSZTNOGI'
