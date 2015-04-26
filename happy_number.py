class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        lookup = {}
        num = self.helper(n)
        while num not in lookup:
            lookup[num] = 1
            num = self.helper(num)
            if num == 1:
                return True
        return False

    def helper(self, n):
        # get current num
        ret = 0
        while n > 0:
            ret += (n % 10)**2
            n /= 10
        return ret


sol = Solution()
for n in range(100):
    print sol.isHappy(n) ,
