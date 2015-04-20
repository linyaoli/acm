def findRotated(arr, tar):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (l + r)/2
        if arr[m] == tar:
            return m

        if arr[m] < arr[l]:
            if tar > arr[m] and tar <= arr[r]:
                l = m + 1
            else:
                r = m - 1
        else:
            if tar < arr[m] and tar >= arr[l]:
                r = m - 1
            else:
                l = m + 1
    return m


print findRotated([7,8,9,1,2,3,4,5,6], 6)
