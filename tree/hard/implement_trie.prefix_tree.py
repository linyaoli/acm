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

# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("somestring")
trie.insert("ab")
print trie.search("key")
print trie.search("a")
print trie.startsWith("some")
print trie.startsWith("a")
