#generate a set of m integers from an array of size n.
#each element must have equal probility of being chosen.
def pick(arr, m):
    subset = []
    for i in xrange(m):
        subset.append(arr[i])
    for i in xrange(m, len(arr)):
        k = rand(0, i)
        if k < m:
            subset[k] = arr[i]
    return subset
