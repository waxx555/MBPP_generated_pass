'''
Write a python function to count number of substrings with the sum of digits equal to their length.
'''

def count_Substrings(string,n):
    count = 0
    for i in range(n):
        for j in range(i,n):
            if sum(map(int,string[i:j+1])) == j-i+1:
                count += 1
    return count


assert count_Substrings('112112',6) == 6
assert count_Substrings('111',3) == 6
assert count_Substrings('1101112',7) == 12
