class ListNode:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.keys_to_list_node = {}

        self.start = None  # Most recently used
        self.end = None    # Least recently used

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.start = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.end = node.prev

    def add_to_start(self, node):
        node.prev = None
        node.next = self.start

        if self.start:
            self.start.prev = node
        else:
            self.end = node

        self.start = node

    def get(self, key: int) -> int:
        if key not in self.keys_to_list_node:
            return -1

        node = self.keys_to_list_node[key]

        self.remove(node)
        self.add_to_start(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.keys_to_list_node:
            node = self.keys_to_list_node[key]
            node.val = value

            self.remove(node)
            self.add_to_start(node)
            return

        new_node = ListNode(key, value)
        self.keys_to_list_node[key] = new_node
        self.add_to_start(new_node)
        self.count += 1

        if self.count > self.capacity:
            old_end = self.end
            self.remove(old_end)
            del self.keys_to_list_node[old_end.key]
            self.count -= 1