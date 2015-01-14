"""
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

"""
class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        # Radix sort
        # 1. find the length of base-digit of largest num.
        _max = max_num = max(num)
        #base = 1
        #while _max > 10:
            #_max /= 10
            #base *= 10
        base = 10
        # 2. radix sorting in descending order.
        buckets = [[] for _ in range(10)]
        it = 0

        while ((base ** it) <= _max):
            num, buckets = self.buckets_to_list(self.list_to_buckets(num, base, it, buckets))
            it += 1

        result = ''
        for i in num[::-1]:
            result += str(i)

        return result

    def list_to_buckets(self, array, base, iteration, last_buckets):
        buckets = [[] for _ in range(base)]
        #print array, base, iteration
        for number in array:
            if number >= (base ** iteration):
                digit = (number // (base ** iteration)) % base
                buckets[digit].append(number)
            else:
                # if number is smaller, remain the same position.
                for i in xrange(10):
                    #print number, last_buckets
                    if number in last_buckets[i]:
                        buckets[i].extend(last_buckets[i])
                        break
        print buckets
        return buckets

    def buckets_to_list(self, buckets):
        array = []
        for bucket in buckets:
            array.extend(bucket[::-1])
        return array, buckets


sol = Solution()
print sol.largestNumber([12, 128])
