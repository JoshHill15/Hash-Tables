

class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, key, val):
        new_node = HashTableEntry(key, val)
        new_node.next = self.head
        self.head = new_node

    def find(self, key):
        curr = self.head
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next

    def delete(self, key):
        if key == self.head.key:
            self.head = self.head.next
        curr = self.head
        prev = None
        while curr:
            if curr.key == key:
                prev.next = curr.next
            prev = curr
            curr = curr.next


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, storage):
        self.storage = [None] * storage
        self.capacity = storage

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for letter in key:
            hash = ((hash << 5) + hash) + ord(letter)
        hash = hash % self.capacity
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.djb2(key)
        if self.storage[index]:
            self.storage[index].insert(key, value)
        else:
            self.storage[index] = LinkedList()
            self.storage[index].insert(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.djb2(key)
        self.storage[index].delete(key)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.djb2(key)
        if self.storage[index]:
            return self.storage[index].find(key)
        else:
            return None

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        self.storage = self.storage * 2
        self.capacity = self.capacity * 2


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")
    # # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
    # test delete
    ht.delete("line_3")
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")

    # l = LinkedList()
    # l.insert("a", 1)
    # l.insert("b", 2)
    # l.insert("c", 3)
    # l.insert("d", 4)
    # print(l.head.key, l.head.value)
    # print(l.head.next.key, l.head.next.value)
    # print(l.head.next.next.key, l.head.next.next.value)
    # print(l.head.next.next.next.key, l.head.next.next.next.value)
