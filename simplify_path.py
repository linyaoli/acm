class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        saber = [] # word
        word = ""
        for i in xrange(len(path)):
            if path[i] != '/':
                word += path[i]
            else:
                if word == '.':
                    word = "" # do nothing
                elif word == "..":
                    if len(saber) >= 1:
                        saber.pop()
                else:
                    if word != "":
                        saber.append(word)
                word = ""
        if word != "":
            if word == "..":
                if len(saber) >= 1:
                    saber.pop()
            elif word != ".":
                saber.append(word)

        word = ""

        for x in xrange(len(saber)):
            word += "/" + saber[x]
        if word == "":
            return '/'
        return word
