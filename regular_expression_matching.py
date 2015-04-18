"""
'.' matches one character.
'*' matches zero or more of preceding element.

if P[j+1] != '*'
    1. S[i] == P[j] => isMatch(i+1, j+1)
    2. S[i] != P[j] => false

if P[j+1] == '*'
    1. S[i] == P[j] => isMatch(i+1, j+2) or (i, j+2)
    2. S[i] != P[j] => isMatch(i,j+2)

if S[i] == '\0' and P[j] == '\0' => True

"""
class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        dp = [[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0] = True

        for i in range(1,len(p)+1):
            if p[i-1] == '*' and i >= 2:
                dp[0][i] = dp[0][i-2]

        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                ########################################
                if p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    # match 1 or 0 preceding element.
                    dp[i][j] = dp[i][j-1] or dp[i][j-2] or \
                    # match multiple preceding elements
                    (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.')) # or match '.'
                else:
                    dp[i][j] = dp[i-1][j-1] and s[i-1] == p[j-1]

        return dp[-1][-1]

    def isMatch_TLE(self, s, p):
        if len(p)==0: return len(s)==0
        if len(p)==1 or p[1]!='*':
            if len(s)==0 or (s[0]!=p[0] and p[0]!='.'):
                return False
            return self.isMatch(s[1:],p[1:])
        else:
            i=-1; length=len(s)
            while i<length and (i<0 or p[0]=='.' or p[0]==s[i]):
                if self.isMatch(s[i+1:],p[2:]): return True
                i+=1
            return False

    def isMatch_t(self, s, p):
        return self.helper(s, 0, p, 0)

    def helper(self, s, i, p, j):
        if j >= len(p): return i >= len(s)
        #next char is not '*': must match current character
        if (j == len(p) - 1 or p[j + 1] != '*') and i < len(s):
            return (p[j] == s[i] or (p[j] == '.' and i < len(s))) \
                and self.helper(s, i + 1, p, j + 1)
        #next char is '*'
        while ( i < len(s) and p[j] == '.' ) or \
            (i < len(s) and j < len(p) and s[i] == p[j]) or \
            (i == len(s) and j == len(p)):
          # p[j] == s[i]:
            if self.helper(s, i, p, j + 2):
                return True
            i += 1

        return self.helper(s, i, p, j + 2)


sol = Solution()
print sol.isMatch_TLE('aaaaaaaaaaaaab', 'a*a*a*a*a*a*a*a*a*a*c')
