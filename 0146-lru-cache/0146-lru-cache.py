class Node:
    def __init__(self,key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

# build double linkedlist + hashmap (dict in python)
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # hashmap from key --> Node
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

    def _remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
    
    def _insert(self,node):
        first_real_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = first_real_node
        first_real_node.prev = node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)