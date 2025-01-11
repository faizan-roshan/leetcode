# LeetCode URL: https://leetcode.com/problems/lru-cache/description/

from collections import OrderedDict


class LRUCache:
    """
    This is using the OrderedDict() from python Collections.
    """

    def __init__(self, capacity: int):

        self.lru = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:

        if self.lru.get(key) is not None:
            self.lru.move_to_end(key, last=False)
            return self.lru[key]
        return -1

    def put(self, key: int, value: int) -> None:

        if self.lru.get(key) is None:

            if len(self.lru) >= self.capacity:

                self.lru.popitem()

            self.lru[key] = value
            self.lru.move_to_end(key, last=False)

        else:
            self.lru[key] = value
            self.lru.move_to_end(key, last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
