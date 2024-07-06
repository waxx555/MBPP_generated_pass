'''
Write a function to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
'''

def change_date_format(date):
    return '-'.join(date.split('-')[::-1])


assert change_date_format('2026-01-02')=='02-01-2026'
assert change_date_format('2021-01-04')=='04-01-2021'
assert change_date_format('2030-06-06')=='06-06-2030'
