def removeDup(nums):
    j = 0
    for i in xrange(1, len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
    print nums[:j+1]

def removeAllDup(nums):
    j = 0
    i = 0
    while i < len(nums):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
        i += 1

    print nums
removeAllDup([1,2,2,2,2,4])
