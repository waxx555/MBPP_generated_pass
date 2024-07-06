'''
Write a python function to check whether a given sequence is linear or not.
'''

def Seq_Linear(seq):
    if len(seq) < 3:
        return "Linear Sequence"
    diff = seq[1] - seq[0]
    for i in range(2, len(seq)):
        if seq[i] - seq[i-1] != diff:
            return "Non Linear Sequence"
    return "Linear Sequence"


assert Seq_Linear([0,2,4,6,8,10]) == "Linear Sequence"
assert Seq_Linear([1,2,3]) == "Linear Sequence"
assert Seq_Linear([1,5,2]) == "Non Linear Sequence"
