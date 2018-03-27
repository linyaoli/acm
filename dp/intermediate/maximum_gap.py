"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

"""

class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        #bucket sorting
        n = len(num)
        if n < 2:
            return 0
        # find min and max in list O(n)
        MIN, MAX = min(num), max(num)
        # divided range of each bucket
        bucket_range = max(1, int((MAX - MIN - 1) / (n - 1)) + 1)        
        bucket_len = (MAX - MIN) / bucket_range + 1
        buckets = [None for _ in xrange(bucket_len)]

        for i in num:
            bucket_idx = (i - MIN) / bucket_range
            bucket = buckets[bucket_idx]
            if not bucket:
                bucket = {'min': i, 'max': i}
                buckets[bucket_idx] = bucket
            else:
                bucket['min'] = min(bucket['min'], i)
                bucket['max'] = max(bucket['max'], i)
        print buckets
        max_gap = 0
        for x in xrange(bucket_len):
            if buckets[x] is None:
                continue
            y = x + 1
            while y < bucket_len and buckets[y] is None:
                y += 1
            if y < bucket_len:
                max_gap = max(max_gap, buckets[y]['min'] - buckets[x]['max'])
            x = y

        return max_gap


sol = Solution()
print sol.maximumGap([8, 10, 4, 2, 1, 7, 9])
