class Node:
    def __init__(self, val):
        self.val = val
        self.next = {}

def insert(root, word):
    cur = root
    for i in xrange(len(word)):
        if word[i] not in cur.next:
            node = Node(word[i])
            cur.next[word[i]] = node
        cur = cur.next[word[i]]

def find(root, word):
    cur = root

if __name__ == "__main__":
    root = Node("")
    insert(root, "lileeyao")
    insert(root, "woshisha")
    insert(root, "lilkk")
    insert(root, "lilka")

    queue = [root]
    while queue != []:
        tmp = []
        while queue != []:
            node = queue.pop(0)
            for i in node.next.keys():
                tmp.append(node.next[i])
        if tmp != []:
            for i in tmp:
                print i.val,
            queue += tmp
        print
