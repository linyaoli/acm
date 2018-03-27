import random as rd
#choose m elems randomly from arr.
def gen(arr, m):
    subset = [0 for _ in xrange(m)]
        
    for i in xrange(m):
        subset[i] = arr[i]

    for i in xrange(m, len(arr)):
        k = (int)(rd.random() * i)
        if k < m:
            subset[k] = arr[i]

    print subset

gen([1,2,3,4,5,6,7,8,9], 5)
