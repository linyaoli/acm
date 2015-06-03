"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string

containing only letters a-z or '.' (A '.' means it can represent any one letter).

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

You may assume that all words are consist of lowercase letters a-z.


"""
class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.val = ""
        self.count = 0
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                tmp = TrieNode()
                node.children[letter] = tmp
                node = tmp
            else:
                node = node.children[letter]
        node.count += 1

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        node = self.root
        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                return False
        if node.count > 0:
            return True
        else:
            return False
    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        node = self.root
        for letter in prefix:
            if letter in node.children:
                node = node.children[letter]
            else:
                return False

        return True

class WordDictionary:

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    book = Trie()
    def addWord(self, word):
        self.book.insert(word)

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        if '.' in list(word):
            return self.helper(word)
        else:
            return self.book.search(word)

    def helper(self, word):
        pass

    def helper_bfs(self, word):#bfs
        queue = [("", -1)]
        while queue != []:
            node = queue.pop(0)

            if node[1] == len(word) - 1:
                if self.book.search(node[0]): return True
                else:
                    continue

            if word[node[1] + 1] != '.':
                queue.append((node[0] + word[node[1] + 1], node[1] + 1))
            else:
                for i in xrange(26):
                    #print node[0] + chr(ord('a') + i)
                    if self.book.startsWith(node[0] + chr(ord('a') + i)):
                        queue.append((node[0] + chr(ord('a') + i), node[1] + 1))

        return False

    def helper_dfs(self, i, kwd, word):
        if i == len(word):
            if self.book.search(kwd):
                self.ret = True
        else:
            for p in xrange(i, len(word)):
                if word[p] == '.':
                    for j in xrange(26):
                        kwd += chr(ord('a') + j)
                        if self.book.startsWith(kwd):
                            self.helper(p + 1, kwd, word)
                        kwd = kwd[:-1]
                else:
                    kwd += word[p]
                    if not self.book.startsWith(kwd):
                        break
                if self.ret: return

            if p == len(word) - 1 and self.book.search(kwd):
                    self.ret = True


# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print wordDictionary.search("pad")
print wordDictionary.search("bad")
print wordDictionary.search(".ad")
print wordDictionary.search("b..")
print wordDictionary.search(".c.")
