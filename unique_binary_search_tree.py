class Solution:
    # @return an integer
    # Count[i] = ∑ Count[0...k] * [ k+1....i]     0<=k<i-1
    # Will recursion solve this problem?
    # ------------------------------------------------------------------
    # 以i为根节点的树，其左子树由[0, i-1]构成， 其右子树由[i+1, n]构成。
    # ------------------------------------------------------------------
    def numTrees(self, n):
        count = [0] * (n + 1)
        count[0] = 1
        count[1] = 1

        if n >= 2:
            for i in xrange(2, n+1):
                for j in xrange(0, i):
                    count[i] += count[j] * count[i - j - 1]

        return count[n]


            
