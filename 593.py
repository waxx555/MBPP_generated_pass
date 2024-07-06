'''
Write a function to remove leading zeroes from an ip address.
'''

def removezero_ip(ip):
    return '.'.join([str(int(i)) for i in ip.split('.')])


assert removezero_ip("216.08.094.196")==('216.8.94.196') 
assert removezero_ip("12.01.024")==('12.1.24') 
assert removezero_ip("216.08.094.0196")==('216.8.94.196') 
