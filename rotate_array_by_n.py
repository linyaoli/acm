# rotate array by n
# do it in O(1) space.

def rotate(arr, n):
    # reverse all
    i, j = 0, len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    # reverse by length
    i, j = 0, len(arr) - n - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    i = len(arr) - n
    j = len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr


print rotate([1,2,3,4,5,6,7,8,9], 3)
#[4,5,6,7,8,9,1,2,3]
