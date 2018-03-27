class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        result = []
        prevMap = {}
        n = len(start)
        for i in dict: prevMap[i] = []
        candidates = [set(),set()]
        cur = 0
        prev = 1
        candidates[cur].add(start)
        while True:
            cur, prev = prev, cur
            for i in candidates[prev]:
                try:
                    dict.remove(i)
                except:
                    continue
            candidates[cur].clear()
            for word in candidates[prev]:
                for i in range(n):
                    part1 = word[:i]
                    part2 = word[i+1:]
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if word[i] != j:
                            nextword = part1 + j + part2
                            if nextword in dict:
                                prevMap[nextword].append(word)
                                candidates[cur].add(nextword)

            if len(candidates[cur]) == 0: return result
            if end in candidates[cur]: break
        self.buildpath([], end, result, prevMap)
        return result

    def buildpath(self, path, word, result, prevMap):
        if len(prevMap[word])==0:
            path.append(word); currPath=path[:]
            currPath.reverse(); result.append(currPath)
            path.pop();
            return
        path.append(word)
        for iter in prevMap[word]:
            self.buildpath(path, iter, result, prevMap)
        path.pop()

sol = Solution()
print sol.findLadders("hit", "cog", ["hot","dot","dog","lot","log"])
