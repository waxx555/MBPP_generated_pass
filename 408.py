'''
Write a function to find k number of pairs which consist of one element from the first array and one element from the second array.
'''

def k_smallest_pairs(nums1, nums2, k):
    res = []
    for i in nums1:
        for j in nums2:
            res.append([i, j])
    return sorted(res, key=lambda x: x[0] + x[1])[:k]


assert k_smallest_pairs([1,3,7],[2,4,6],2)==[[1, 2], [1, 4]]
assert k_smallest_pairs([1,3,7],[2,4,6],1)==[[1, 2]]
assert k_smallest_pairs([1,3,7],[2,4,6],7)==[[1, 2], [1, 4], [3, 2], [1, 6], [3, 4], [3, 6], [7, 2]]
