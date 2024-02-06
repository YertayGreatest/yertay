def perm(string):
    length = len(string)
    permutation = 1
    for i in range(1,length+1):
        permutation = permutation * i
    return permutation
print(perm("string"))


'''import math
def perm2(s):
    return math.factorial(len(s))
'''

