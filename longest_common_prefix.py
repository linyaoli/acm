class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if strs == []:
          return ""
        maxCP = strs[0]
        for _str in strs:
          if len(maxCP) <= len(_str) and maxCP != _str[:len(maxCP)]:
            _len = len(maxCP)
            for i in xrange(len(maxCP) - 1, -1, -1):
              if maxCP[i] != _str[i]:
                _len = i
            maxCP = maxCP[:_len]
          elif len(maxCP) > len(_str):
            if maxCP[:len(_str)] == _str:
              maxCP = _str
            else:
              for i in xrange(len(_str)):
                if maxCP[i] != _str[i]:
                  break
              maxCP = maxCP[:i]

        return maxCP


sol = Solution()
print sol.longestCommonPrefix([" 123 sd12 1a", "123 sdasdasdasd"])
