class Solution:
    # @return a string
    def longestPalindrome(self, s):
        n = len(s)
        if n < 2:
            return s
        longest = s[0]
        for i in xrange(n - 1):
            # even
            p1 = self.isPalindrome(s, i, i);
            if len(p1) > len(longest):
                longest = p1
            # odd
            p2 = self.isPalindrome(s, i, i + 1)
            if len(p2) > len(longest):
                longest = p2

        return longest

    def isPalindrome(self, s, l, r):
        n = len(s)
        while l >= 0 and r < n and (s[l] == s[r]):
            l -= 1
            r += 1
        return s[l+1:r]


sol = Solution()
#print sol.longestPalindrome('abbba')
print sol.longestPalindrome("jhgtrclvzumufurdemsogfkpzcwgyepdwucnxrsubrxadnenhvjyglxnhowncsubvdtftccomjufwhjupcuuvelblcdnuchuppqpcujernplvmombpdttfjowcujvxknzbwmdedjydxvwykbbamfnsyzcozlixdgoliddoejurusnrcdbqkfdxsoxxzlhgyiprujvvwgqlzredkwahexewlnvqcwfyahjpeiucnhsdhnxtgizgpqphunlgikogmsffexaeftzhblpdxrxgsmeascmqngmwbotycbjmwrngemxpfakrwcdndanouyhnnrygvntrhcuxgvpgjafijlrewfhqrguwhdepwlxvrakyqgstoyruyzohlvvdhvqmzdsnbtlwctetwyrhhktkhhobsojiyuydknvtxmjewvssegrtmshxuvzcbrabntjqulxkjazrsgbpqnrsxqflvbvzywzetrmoydodrrhnhdzlajzvnkrcylkfmsdode")
