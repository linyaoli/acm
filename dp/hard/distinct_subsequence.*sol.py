class Solution:
    # @return an integer
    def numDistinct(self, S, T):
    #子串的长度为 i,我们要求的就是长度为 i 的字串在长度为 j 的母串中出现的次数, 设为t[i][j].
    #
    #若母串的最后一个字符与子串的最后一个字符不同,则长度为 i 的子串在长度为 j 的母串中出现的次数
    #就是母串的前 j - 1 个字符中子串出现的次数,即 t[i][j] = t[i][j - 1],
    #
    #若母串的最后一个字符与子串的最后一个字符相同，
    #那么除了前 j - 1 个字符出现字串的次数外,还要加上子串的前 i - 1 个字符
    #
    #在母串的前 j - 1 个字符中出现的次数,即 t[i][j] = t[i][j - 1] + t[i - 1][j - 1].
    #也可以用二维数组，这里图省事，直接用滚动数组了.
        match = [0] * 200
        len_s = len(S)
        len_t = len(T)
        if len_s < len_t :
            return 0
        match[0] = 1
        for i in xrange(1, len_t + 1):
            match[i] = 0
        for i in xrange(1, len_s + 1):
            for j in xrange(len_t, 0, -1):
                if S[i - 1] == T[j - 1]:
                    match[j] += match[j - 1]
        return match[len_t]
