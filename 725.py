'''
Write a function to extract values between quotation marks of the given string by using regex.
'''

import re

def extract_quotation(s):
    return re.findall(r'"(.*?)"', s)


assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
assert extract_quotation('Cast your "favorite" entertainment "apps"') == ['favorite', 'apps']
assert extract_quotation('Watch content "4k Ultra HD" resolution with "HDR 10" Support') == ['4k Ultra HD', 'HDR 10']
