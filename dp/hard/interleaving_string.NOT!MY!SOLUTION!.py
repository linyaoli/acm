class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        match = [False for i in xrange(len(s2) + 1)]
        match[0] = True
        for i in xrange(1, len(s2) + 1):
            match[i] = (s2[i - 1] == s3[i - 1])
        for i in xrange(1, len(s1) + 1):
            match[0] = (s1[i - 1] == s3[i - 1])
            for j in xrange(1, len(s2) + 1):
                match[j] = (match[j - 1] and (s2[j - 1] == s3[i + j - 1])) or \
                    (match[j] and (s1[i - 1] == s3[i +j - 1]));
        return match[len(s2)]
"""
        Match[i][j]
    =   (s3.lastChar == s1.lastChar) && Match[i-1][j]
      ||(s3.lastChar == s2.lastChar) && Match[i][j-1]
初始条件：
    i=0 && j=0 时，Match[0][0] = true;
    i=0时， s3[j] = s2[j], Match[0][j] |= Match[0][j-1]
           s3[j] != s2[j], Match[0][j] = false;

    j=0时， s3[i] = s1[i], Match[i][0] |= Match[i-1][0]
           s3[i] != s1[i], Match[i][0] = false;
           """
