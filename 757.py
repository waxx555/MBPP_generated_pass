'''
Write a function to count the pairs of reverse strings in the given string list.
'''

def count_reverse_pairs(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j][::-1]:
                count += 1
    return str(count)


assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== '2'
assert count_reverse_pairs(["geeks", "best", "for", "skeeg"]) == '1'
assert count_reverse_pairs(["makes", "best", "sekam", "for", "rof"]) == '2' 
