'''
Write a python function to count the pairs with xor as an odd number.
'''

def find_Odd_Pair(lst,n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if (lst[i] ^ lst[j]) % 2 != 0:
                count += 1
    return count


assert find_Odd_Pair([5,4,7,2,1],5) == 6
assert find_Odd_Pair([7,2,8,1,0,5,11],7) == 12
assert find_Odd_Pair([1,2,3],3) == 2
