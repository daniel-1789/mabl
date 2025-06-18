from functools import lru_cache


class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, cache_max):
        self.cache_max = cache_max
        self.lru_ptrs = dict()
        self.head = Node("h", "head")
        self.tail = Node("t", "tail")
        self.head.next = self.tail
        self.tail.prev = self.head

    def delnode(self, node:Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def insert_head(self, node:Node):
        old_next = self.head.next
        self.head.next = node
        node.next = old_next
        node.prev = self.head
        old_next.prev = node

    def put(self, k, v):
        # see if currently in cache
        curr_node:Node = self.lru_ptrs.get(k)

        if curr_node:
            self.delnode(curr_node)
            curr_node.next = None
            curr_node.prev = None
            curr_node.value = v
        else:
            curr_node = Node(k=k, v=v)

            if len(self.lru_ptrs) == self.cache_max:
                # pop the end of the cache
                del_node:Node = self.tail.prev
                self.delnode(del_node)
                self.lru_ptrs.pop(del_node.key)

            self.lru_ptrs[k] = curr_node

        self.insert_head(curr_node)

    def get(self, k):
        node:Node = self.lru_ptrs.get(k)
        if node is None:
            return -1

        self.delnode(node)
        self.insert_head(node)

        return node.value
