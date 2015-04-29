class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        v1 = version1.split('.')
        v2 = version2.split('.')
        len_min = min(len(v1), len(v2))
        for i in xrange(len_min):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
            else:
                pass

        if len(v1) > len(v2):
            for i in xrange(len(v2), len(v1)):
                if int(v1[i]) > 0:
                    return 1
        elif len(v1) < len(v2):
            for i in xrange(len(v1), len(v2)):
                if int(v2[i]) > 0:
                    return -1
        else:
            pass

        return 0


sol = Solution()
print sol.compareVersion('01', '1')
print sol.compareVersion('1', '1.0')
print sol.compareVersion('1.0.0.1', '1.0')
print sol.compareVersion('1', '2.0')
