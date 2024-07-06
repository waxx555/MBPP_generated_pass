'''
## write a function to find the minimum number of jumps to reach the end of the array for the given array of integers where each element represents the max number of steps that can be made forward from that element. > indented block > indented block
'''

def min_jumps(arr, n):
    if n <= 1:
        return 0
    if arr[0] == 0:
        return -1
    max_reach = arr[0]
    steps = arr[0]
    jumps = 1
    for i in range(1, n):
        if i == n - 1:
            return jumps
        max_reach = max(max_reach, i + arr[i])
        steps -= 1
        if steps == 0:
            jumps += 1
            if i >= max_reach:
                return -1
            steps = max_reach - i
    return -1


assert min_jumps([1, 3, 6, 1, 0, 9], 6) == 3
assert min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9], 11) == 3
assert min_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 11) == 10
