class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        #remove all non-alphanumic chas
        n = len(s)
        l = 0
        r = n - 1
        while l <= r - 1:
            while not s[l].isalpha() and not s[l].isdigit() and l <= r - 1:
                l += 1
            while not s[r].isalpha() and not s[r].isdigit() and l <= r - 1:
                r -= 1

            if s[l].upper() != s[r].upper():
                return False
            l += 1
            r -= 1

        return True

sol = Solution()
print sol.isPalindrome("1a2")
print sol.isPalindrome("A man, a plan, a canal: Panama")
