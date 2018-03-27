"""
given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3]

"""
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        res = []
        self.target = target
        self.candidates = candidates
        self.gen(0, res, [])
        return res

    def gen(self, i, res, sol):
        if sum(sol) == self.target:
            res.append(sorted(sol[:]))
        elif sum(sol) > self.target or i == len(self.candidates):
            return
        else:
            for j in xrange(i, len(self.candidates)):
                sol.append(self.candidates[j])
                self.gen(j, res, sol)
                sol.pop()


sol = Solution()
print sol.combinationSum([1,2,3,4,5,6,7], 5)
