'''
Write a function to convert a date of yyyy-mm-dd format to dd-mm-yyyy format by using regex.
'''

import re

def change_date_format(date):
    return re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3-\2-\1', date)


assert change_date_format("2026-01-02") == '02-01-2026'
assert change_date_format("2020-11-13") == '13-11-2020'
assert change_date_format("2021-04-26") == '26-04-2021'
