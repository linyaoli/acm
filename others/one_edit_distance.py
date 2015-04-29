"""
Question:
Given two strings S and T, determine if they are both one edit distance apart.
Hint:
1. If |n-m| is greater than 1, we know immediately both are not one edit distance apart.
2. It might help if you consider these cases separately, m == n and m != n
3. Assume that m is always <= n, which greatly simplifies the conditional statements.
If m > n, we could just simply swap S and T.
4. If m == n, it becomes finding if there is exactly one modified operation. If m != n
, you do not have to consider the delete operation. Just consider the insert operation in T.

"""
class Solution :
    def oneEditDist(self, t, s):
        # replace, insert, append
        # assume target is longer than source.
        assert len(t) >= len(s) and len(t) - len(s) < 2
        diff = len(t) - len(s)
        i = 0
        while i < len(s) and s[i] == t[i]: i+= 1
        if i == len(s): return diff > 0
        if diff == 0: i += 1
        # skip the nonmatching char and make sure if the left chars are the same.
        while i < len(s) and s[i] == t[i + diff]: i+= 1
        return i == len(s)


sol = Solution()
print sol.oneEditDist("lileeyao", "lileeao")
