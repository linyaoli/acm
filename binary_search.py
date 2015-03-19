def b_search(ls, tar):
    n = len(ls)
    start = 0
    end = n - 1
    while start <= end:
        # avoid overflow
        mid = start + ((end - start) >> 1)
        if ls[mid] > tar:
            end = mid - 1
        elif ls[mid] < tar:
            start = mid + 1
        else:
            return True

    return False

ls = [1,3,4,5,6,7,8,10]
print b_search(ls, 9)
