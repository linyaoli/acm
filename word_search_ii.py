"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent"

cells are those horizontally or vertically neighboring. The same letter cell may not be

used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].

"""
import collections
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.flag = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.result = []

    def insert(self, word):
        node = self.root
        for letter in word:
            node = node.children[letter]
        node.flag = True

    def findWords(self, board, words):
        for w in words:
            self.insert(w)
        for i in xrange(len(board)):
            board[i] = list(board[i])

        for j in range(len(board)):
            for i in range(len(board[0])):
                self.helper(self.root, board, j, i)
        return self.result

    def helper(self, node, board, j, i, word=''):
        if node.flag:
            self.result.append(word)
            node.flag = False
        if 0 <= j < len(board) and 0 <= i < len(board[0]):
            char = board[j][i]
            child = node.children.get(char)
            if child is not None:
                word += char
                board[j][i] = None
                self.helper(child, board, j + 1, i, word)
                self.helper(child, board, j - 1, i, word)
                self.helper(child, board, j, i + 1, word)
                self.helper(child, board, j, i - 1, word)
                board[j][i] = char



sol = Solution()
#print sol.findWords(["aaaa","aaaa","aaaa"], ["aaaaaaaaaaaa","aaaaaaaaaaaaa","aaaaaaaaaaab"])
print sol.findWords(["baabab","abaaaa","abaaab","ababba","aabbab","aabbba","aabaab"], ["bbaabaabaaaaabaababaaaaababb","aabbaaabaaabaabaaaaaabbaaaba","babaababbbbbbbaabaababaabaaa","bbbaaabaabbaaababababbbbbaaa","babbabbbbaabbabaaaaaabbbaaab","bbbababbbbbbbababbabbbbbabaa","babababbababaabbbbabbbbabbba","abbbbbbaabaaabaaababaabbabba","aabaabababbbbbbababbbababbaa","aabbbbabbaababaaaabababbaaba","ababaababaaabbabbaabbaabbaba","abaabbbaaaaababbbaaaaabbbaab","aabbabaabaabbabababaaabbbaab","baaabaaaabbabaaabaabababaaaa","aaabbabaaaababbabbaabbaabbaa","aaabaaaaabaabbabaabbbbaabaaa","abbaabbaaaabbaababababbaabbb","baabaababbbbaaaabaaabbababbb","aabaababbaababbaaabaabababab","abbaaabbaabaabaabbbbaabbbbbb","aaababaabbaaabbbaaabbabbabab","bbababbbabbbbabbbbabbbbbabaa","abbbaabbbaaababbbababbababba","bbbbbbbabbbababbabaabababaab","aaaababaabbbbabaaaaabaaaaabb","bbaaabbbbabbaaabbaabbabbaaba","aabaabbbbaabaabbabaabababaaa","abbababbbaababaabbababababbb","aabbbabbaaaababbbbabbababbbb","babbbaabababbbbbbbbbaabbabaa"])
