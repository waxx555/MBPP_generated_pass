'''
Write a function to exchange the position of every n-th value with (n+1)th value and (n+1)th value with n-th value in a given list.
'''

def exchange_elements(lst):
    return [lst[i+1] if i%2==0 else lst[i-1] for i in range(len(lst))]



assert exchange_elements([0,1,2,3,4,5])==[1, 0, 3, 2, 5, 4] 
assert exchange_elements([5,6,7,8,9,10])==[6,5,8,7,10,9] 
assert exchange_elements([25,35,45,55,75,95])==[35,25,55,45,95,75] 
