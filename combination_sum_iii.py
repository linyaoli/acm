"""
Find all possible combinations of k numbers that add up to a number n,
given that only numbers from 1 to 9 can be used and each combination
should be a unique set of numbers.

Ensure that numbers within the set are sorted in ascending order.

Input: k = 3, n = 7

Output:

[[1,2,4]]

"""
class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        self.n = n
        self.k = k
        self.ret = []
        self.helper(1, 0, [])
        return self.ret

    def helper(self, i, p, sol):
        if sum(sol) == self.n and p == self.k:
            self.ret.append(sol[:])
        elif sum(sol) > self.n or p > self.k:
            return
        else:
            for j in xrange(i, 10):
                sol.append(j)
                self.helper(j + 1, p + 1, sol)
                sol.pop()

sol = Solution()
print sol.combinationSum3(3, 7)
