class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        res = []
        visited = [0 for _ in xrange(len(num))]
        self.helper(sorted(num), 0, res, visited, [])
        return res

    def helper(self, num, i, res, visited, sol):
        if i == len(num):
            res.append(sol[:])
        else:
            for j in xrange(0, len(num)):
                if visited[j] == 0:
                    if j > 0 and num[j] == num[j-1] and visited[j-1] == 0:
                        continue
                    sol.append(num[j])
                    visited[j] = 1
                    self.helper(num, i+1, res, visited, sol)
                    sol.pop()
                    visited[j] = 0


sol = Solution()
print sol.permuteUnique([1,2,3])
