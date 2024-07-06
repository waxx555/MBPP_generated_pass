'''
Write a python function to find number of integers with odd number of set bits.
'''

def count_With_Odd_SetBits(n):
    count = 0
    for i in range(1,n+1):
        if bin(i).count('1')%2!=0:
            count += 1
    return count


assert count_With_Odd_SetBits(5) == 3
assert count_With_Odd_SetBits(10) == 5
assert count_With_Odd_SetBits(15) == 8
