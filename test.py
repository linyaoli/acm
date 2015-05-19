nums = [3,4,1,-1]
nums= [0,1,2,3]
nums=[1]
n = len(nums)
first = 1
for i in xrange(n):
    while nums[i] != i + 1:
        #print i, nums[i], nums
        if nums[i] < 1 or nums[i] > n or nums[i] == nums[nums[i]-1]:
            first = i + 1
            break
        t = nums[i]
        nums[i], nums[t-1] = nums[t-1], nums[i]

print first
