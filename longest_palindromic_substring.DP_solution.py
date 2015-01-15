class Solution:
    # @return a string
    def longestPalindrome(self, s):
        n = len(s)
        P = [[0 for _ in xrange(n)] for _ in xrange(n)]
        # P[i][j] -> substring s[i:j] is a palindrome or not
        # P[i][j] = True if i == j
        #           s[i] == s[j] if i == j + 1
        #           (s[i] == s[j]) && P[i+1][j-1]
        if n == 1 or n == 0:
            return s
        max_diff = 0
        a = b = 0
        for i in xrange(n):
            P[i][i] = 1
            for j in xrange(i):
                if i == j + 1:
                    P[j][i] = int(s[i] == s[j])
                else:
                    P[j][i] = int((s[i] == s[j]) and P[j + 1][i - 1])

                if P[j][i] == 1 and i - j > max_diff:
                    max_diff = i - j
                    a, b = j, i

        return s[a:b+1]

sol = Solution()
print sol.longestPalindrome("jhgtrclvzumufurdemsogfkpzcwgyepdwucnxrsubrxadnenhvjyglxnhowncsubvdtftccomjufwhjupcuuvelblcdnuchuppqpcujernplvmombpdttfjowcujvxknzbwmdedjydxvwykbbamfnsyzcozlixdgoliddoejurusnrcdbqkfdxsoxxzlhgyiprujvvwgqlzredkwahexewlnvqcwfyahjpeiucnhsdhnxtgizgpqphunlgikogmsffexaeftzhblpdxrxgsmeascmqngmwbotycbjmwrngemxpfakrwcdndanouyhnnrygvntrhcuxgvpgjafijlrewfhqrguwhdepwlxvrakyqgstoyruyzohlvvdhvqmzdsnbtlwctetwyrhhktkhhobsojiyuydknvtxmjewvssegrtmshxuvzcbrabntjqulxkjazrsgbpqnrsxqflvbvzywzetrmoydodrrhnhdzlajzvnkrcylkfmsdode")
