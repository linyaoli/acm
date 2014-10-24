class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        # enumeration costs O(n^4)
        result = []
        tmp = []
        num = sorted(num)
        l = len(num)
        i = 0
        j = l - 1
        for m in xrange(l):
            for n in xrange(l):
                if m != n:
                    i = 0
                    j = l - 1
                    while i < j and i != m and i != n and j != m and j != n:
                        print m, n, i, j, num[m] +  num[n] +  num[i] + num[j]
                        if num[m] + num[n] + num[i] + num[j] < target:
                            i = i + 1
                        elif num[m] + num[n] + num[i] + num[j] > target:
                            j = j - 1
                        else:
                            tmp = sorted([num[m], num[n], num[i], num[j]])
                            if tmp not in result:
                                result.append(tmp)
                            i = i + 1
        print l
        return result

s = Solution()
print s.fourSum([-494, -487, -471, -470, -465, -462, -447,
                 -445, -441,
                 -432, -429, -422, -406, -398, -397, -364,
                 -344, -333, -328,
                 -307, -302, -293, -291, -279, -269, -269,
                 -268, -254, -198, -181,
                 -134, -127, -115, -112, -96, -94, -89, -58,
                 -58, -58, -44, -2, -1, 43, 89,
                 92, 100, 101, 106, 106, 110, 116, 143, 156,
                 168, 173, 192, 231, 248, 256, 281,
                 316, 321, 327, 346, 352, 353, 355, 358, 365,
                 371, 410, 413, 414, 447, 473, 473,
                 475, 476, 481, 491, 498], 8511)
