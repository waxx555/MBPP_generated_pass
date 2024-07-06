'''
Write a function to count the same pair in three given lists.
'''

def count_samepair(lst1,lst2,lst3):
    count = 0
    for i in range(len(lst1)):
        if lst1[i] == lst2[i] == lst3[i]:
            count += 1
    return count


assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3
assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,8],[2,1,3,1,2,6,7,8])==4
assert count_samepair([1,2,3,4,2,6,7,8],[2,2,3,1,2,6,7,8],[2,1,3,1,2,6,7,8])==5
