"""
*** get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.

*** set(key, value) - Set or insert the value if the key is not already present. When the cache
reached its capacity, it should invalidate the least recently used item before inserting a new item.
"""
import collections
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.index = collections.OrderedDict()
        self.capacity = capacity

    # @return an integer
    def get(self, key):
        try:
            tmp = self.index[key]
            del self.index[key]
            self.index[key] = tmp
            return tmp
        except:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        # if the key is already in cache
        # renew it anyway, attach it to the last
        # regardless if reach the capacity
        try:
            del self.index[key]
            self.index[key] = value
            return
        #if the key is not in the cache
        # 1. reach the capacity
        except:
            if len(self.index) == self.capacity:
                self.index.popitem(last = False)
        # 2. not reach the capacity
            self.index[key] = value


sol = LRUCache(1)
sol.set(2, 1)
print sol.get(2)
sol.set(2, 3)
sol.set(3, 2)
print sol.get(2)
print sol.get(3)
