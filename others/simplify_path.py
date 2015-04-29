class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        names = []
        word = ""
        path += "/"
        for i in xrange(len(path)):
            if path[i] != '/':
                word += path[i]
            else:
                if word != "":
                    names.append(word)
                word = ""

        ls = []
        for i in xrange(len(names)):
            if names[i] == '..':
                if ls != []:
                    ls.pop()
            elif names[i] == '.':
                pass
            else:
                ls.append(names[i])

        return '/' + '/'.join(ls)
