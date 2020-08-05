
class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        resu = ''
        current = self.head

        while current is not None:
            resu += f'({current.value})'
            if current.next is not None:
                resu += ' -> '
            current = current.next
        return resu

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    def find(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None

    def delete(self, value):
        current = self.head

        if current.value == value:
            self.head = self.head.get_next
            return current

        prev = current
        current = current.get_next
        while current is not None:
            if current.value == value:
                prev.next = current.next
                return current
            else:
                prev = prev.next
                current = current.get_next
        return None


class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = MIN_CAPACITY
        self.hashmap = [LinkedList()] * self.capacity
        self.size = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.size/self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        return

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        current = self.hashmap[index].head
        while current:
            if current.key == key:
                current.value == value
            current = current.next

        node = HashTableEntry(key, value)
        self.hashmap[index].insert_at_head(node)
        self.size += 1
        # # self.size += 1
        # if self.hash_data[index] is None:
        #     self.hash_data[index] = node
        #     print(self.hash_data[index])
        # else:
        #     if self.hash_data[index].key == key:
        #         self.hash_data[index].value = value
        #     else:
        #         old_head = self.hash_data[index]
        #         node.set_next(old_head)
        #         self.hash_data[index] = node

        # old_head = self.hash_data[index].head
        # node = self.hash_data[index].head
        # node.next = old_head
        # # print(self.hash_data[index].key)
        # return

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here

        self.put(key, None)
        self.size -= 1
        # index = self.hash_index(key)
        # self.hash_data[index] = None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        current = self.hashmap[index].head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

        # while current is not None:
        #     # print(f'current: {current.key}')
        #     # print(f'key: {key}')
        #     if current.key == key:
        #         # print(current)
        #         return current
        #     current = current.next
        # return None

        # index = self.hash_index(key)
        # return self.hash_data[index]

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        if self.get_load_factor() > 0.7:
            old_map = self.hashmap
            self.hashmap = [LinkedList()] * new_capacity
            for item in old_map:
                current = item.head
            while current:
                self.put(current.key, current.value)
                current = current.next
        self.capacity = new_capacity


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
