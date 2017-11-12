class Node:
    left = None
    right = None
    def __init__(self, val, key):
        self.val = val
        self.key = key

class lruCache:
    def __init__(self, size):
        self.keyMap = {}
        self.tail = None
        self.head = None
        self.SIZE = size

    def get(self, key):
        if key not in self.keyMap:
            return "not exist!"
        else:
            self.refresh(key)
            return self.keyMap[key].val

    def set(self, key, val):
        if self.SIZE < 1: return
        if self.keyMap == {}:
            node = Node(val, key)
            self.keyMap[key] = node
            self.tail = node
            self.head = node
        else:
            if key not in self.keyMap:
                node = Node(val, key)
                self.keyMap[key] = node
                self.tail.right = node
                node.left = self.tail
                self.tail = node

                if len(self.keyMap.keys()) > self.SIZE:
                    del self.keyMap[self.head.key]
                    self.head = self.head.right
                    if not self.head:
                        self.head = node
                        self.tail = node
                    else:
                        self.head.left = None

            else:
                self.keyMap[key].val = val
                self.refresh(key)

    def refresh(self, key):
        node = self.keyMap[key]
        if node == self.tail:
            return
        elif node == self.head:
            self.head = self.head.right
            self.head.left = None
        else:
            node.left.right = node.right
            node.right.left = node.left

        self.tail.right = node
        node.left = self.tail
        self.tail = node

lru = lruCache(0)
lru.set('a', 1)
print lru.get('a')

lru = lruCache(1)
lru.set('a', 2)
print lru.get('a')
lru.set('b', 1)
print lru.get('a')
print lru.get('b')

lru = lruCache(3)
lru.set('a', 1)
lru.set('b', 2)
lru.set('c', 3)
print lru.keyMap
lru.get('a')
lru.get('b')
lru.set('d', 4)
print lru.keyMap
lru.set('e', 4)
print lru.keyMap
