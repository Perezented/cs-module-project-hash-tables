class Node:   # This corresponds to the HashTableEntry class
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:  # This corresponds to the HashTable class
    def __init__(self):
        self.head = None

    def find(self, value):
        cur = self.head
        while cur is not None:
            if cur.value == value:
                return cur
            cur = cur.next
        # If we get to this point, we did not find it
        return None

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    def delete(self, value):
        if self.head.value = value:
            old_head = self.head
            self.head = self.head.next
            return old_head

        prev = self.head
        cur = self.head.next

        while cur is not None:
            if cur.value == value:

                return cur
            prev = prev.next
            cur = cur.next
        return None
