class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        # enumeration costs O(n^4)
        result = []
        tmp = []
        num = sorted(num)
        l = len(num)
        pairs = {}
        # store all results of pairs
        for m in xrange(l - 1):
            for n in xrange(m + 1, l):
                k = num[m] + num[n]
                if k not in pairs:
                    pairs[k] = [(m, n)]
                else:
                    pairs[k].append((m, n))

        n = len(pairs)
        i = 0
        j = l - 1
        for i in xrange(l - 1):
            for j in xrange(i + 1, l):
                tmp = num[i] + num[j]
                res = target - tmp
                if res in pairs:
                    for kk in pairs[res]:
                        rr = sorted([num[i], num[j], num[kk[0]], num[kk[1]]])
                        if rr not in result and i != kk[0] and j != kk[0] and i != kk[1] and j != kk[1]:
                            result.append(rr)

        return result
# -2 -1 0 0 1 2
s = Solution()
print s.fourSum([1,0,-1,0,-2,2], 0)
