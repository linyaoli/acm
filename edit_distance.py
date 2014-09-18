class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        matchUp = [0] * 20000
        matchDown = [0] * 20000
        len_a = len(word1)
        len_b = len(word2)

        for i in xrange(max(len_a, len_b) + 1):
            matchUp[i] = 0
            matchDown[i] = i
        for i in xrange(1, len_a + 1):
            matchUp[0] = i
            for j in xrange(1, len_b + 1):
                if word1[i - 1] == word2[j - 1]:
                    matchUp[j] = matchDown[j - 1]
                else:
                    matchUp[j] = min(matchDown[j], matchDown[j - 1])
                    matchUp[j] = min(matchUp[j], matchUp[j - 1]) + 1
            matchUp, matchDown = matchDown, matchUp

        return matchDown[len_b]
        
