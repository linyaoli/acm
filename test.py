class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        stack = []
        word = ""
        path += "/"
        n = len(path)
        i = 0
        point = 0
        while i < n:
            if path[i] != '/':
                word += path[i]
            else:
                if word != "":
                    stack.append(word)
                word = ""
            i += 1

        res = ""
        i = 0
        ls = []
        while i < len(stack):
            if stack[i] == '..':
                if ls != []:
                    ls.pop()
            elif stack[i] == '.':
                pass
            else:
                ls.append(stack[i])
            i += 1

        return '/' + '/'.join(ls)


sol = Solution()
print sol.simplifyPath("/home/")
