'''
Write a function to find the most common elements and their counts of a specified text.
'''

def most_common_elem(txt, n):
    from collections import Counter
    return Counter(txt).most_common(n)


assert most_common_elem('lkseropewdssafsdfafkpwe',3)==[('s', 4), ('e', 3), ('f', 3)] 
assert most_common_elem('lkseropewdssafsdfafkpwe',2)==[('s', 4), ('e', 3)]
assert most_common_elem('lkseropewdssafsdfafkpwe',7)==[('s', 4), ('e', 3), ('f', 3), ('k', 2), ('p', 2), ('w', 2), ('d', 2)]
