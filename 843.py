'''
Write a function to find the nth super ugly number from a given prime list of size k using heap queue algorithm.
'''

import heapq

def nth_super_ugly_number(n, primes):
    heap = [1]
    for i in range(n):
        num = heapq.heappop(heap)
        for prime in primes:
            heapq.heappush(heap, num*prime)
            if num%prime==0:
                break
    return num


assert nth_super_ugly_number(12,[2,7,13,19])==32
assert nth_super_ugly_number(10,[2,7,13,19])==26
assert nth_super_ugly_number(100,[2,7,13,19])==5408
