'''
Write a python function to count the pairs with xor as an even number.
'''

def find_even_Pair(arr,n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if (arr[i]^arr[j])%2 == 0:
                count += 1
    return count


assert find_even_Pair([5,4,7,2,1],5) == 4
assert find_even_Pair([7,2,8,1,0,5,11],7) == 9
assert find_even_Pair([1,2,3],3) == 1
