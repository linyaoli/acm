class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
        if len(s1) == 1 and len(s2) == 1:
            return s1[0] == s2[0]
        t1 = sorted(list(s1))
        t2 = sorted(list(s2))

        if t1 != t2:
            return False
        if s1 == s2:
            return True
        for i in xrange(1, len(s1)):
            s11 = s1[:i]
            s12 = s1[i:]
            s21 = s2[:i]
            s22 = s2[i:]
            if self.isScramble(s11, s21) and self.isScramble(s12, s22):
                return True
            s21 = s2[:len(s2) - i]
            s22 = s2[len(s2) -i:]
            if self.isScramble(s11, s22) and self.isScramble(s12, s21):
                return True
        return False

sol = Solution()
print sol.isScramble("rgeat", "great")
