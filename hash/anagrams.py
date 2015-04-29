class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        lookup = {}
        for word in strs:
            after_word = sorted(word)
            sorted_word = "".join(after_word)

            try:
                lookup[sorted_word].append(word)
            except:
                lookup[sorted_word] = [word]

        res = []
        for key in lookup.keys():
            if len(lookup[key]) > 1:
                res += lookup[key]        

        return res
