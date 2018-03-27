"""
You are given a string, s, and a list of words, words, that are all of the same
 length. Find all starting indices of substring(s) in s that is a concatenation
 of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).

"""
class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        res = []
        n = len(words)
        ls = len(s)
        if n == 0: return []
        str_len = len(words[0])
        # count occurance
        map_str = dict((x, words.count(x)) for x in set(words))

        i = 0
        while i + n * str_len - 1 < ls: # if s[i:] is longer than the concatenation length.
            map_str2 = {}
            j = 0
            while j < n:
                # check the word by length.
                word = s[i + j * str_len : i + (j + 1)* str_len]
                if not word in map_str:
                    break
                else:
                    # if map_str2[word] does not exist, set to 0.
                    map_str2[word] = map_str2.get(word, 0) + 1
                    if map_str2[word] > map_str[word]:
                        break
                    j += 1
            if j == n: res.append(i)
            i += 1

        return res
sol =Solution()
print sol.findSubstring("barfoothefoobarman", ["foo","bar"])
