'''
Write a python function to convert a string to a list.
'''

def Convert(s):
    return s.split()


assert Convert('python program') == ['python','program']
assert Convert('Data Analysis') ==['Data','Analysis']
assert Convert('Hadoop Training') == ['Hadoop','Training']
