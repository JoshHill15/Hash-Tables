


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

    def replace(self, key, val):
        curr = self.head
        while curr:
            if curr.key == key:
                curr.value = val
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

    def print_all(self):
        curr = self.head
        while curr:
            print("node in linked list", curr.value)
            curr = curr.next

    def all_nodes(self):
        curr = self.head
        arr = []
        while curr:
            arr.append(curr)
            curr = curr.next
        return arr


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, storage):
        self.storage = [None] * storage
        self.capacity = storage
        self.load_balance = 0

    def load_balance_ratio(self):
        return self.load_balance / self.capacity

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
            if self.storage[index].find(key) is not None:
                self.storage[index].replace(key, value)
            else:
                self.storage[index].insert(key, value)
                self.load_balance += 1
        else:
            self.storage[index] = LinkedList()
            self.storage[index].insert(key, value)
            self.load_balance += 1
        if self.load_balance_ratio() > 0.7:
            self.double_size()

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.djb2(key)
        if self.storage[index].find(key) is not None:
            self.storage[index].delete(key)
            self.load_balance -= 1

        if self.load_balance_ratio() < 0.2 and self.capacity > 8:
            self.half_size()

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

    def double_size(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        nodes = []
        for i in range(self.capacity):
            if self.storage[i] is not None:
                nodes += self.storage[i].all_nodes()
        self.capacity = self.capacity * 2
        new_storage = [None] * self.capacity
        self.storage = new_storage
        self.load_balance = 0
        for node in nodes:
            self.put(node.key, node.value)

    def half_size(self):
        nodes = []
        for i in range(self.capacity):
            if self.storage[i] is not None:
                nodes += self.storage[i].all_nodes()
        self.capacity = self.capacity // 2
        new_storage = [None] * self.capacity
        self.storage = new_storage
        self.load_balance = 0
        for node in nodes:
            self.put(node.key, node.value)


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled bcapacity")
    ht.put("line_3", "Linked list saves the day!")
    ht.put("line_3", "this is new")
    ht.put("line_4", "this is 4")
    ht.put("line_5", "this is 5")
    old_capacity = len(ht.storage)
    ht.put("line_6", "this is 6")
    print("percentage", str(ht.load_balance_ratio())+"%")
    # print("")
    # # # # Test storing beyond capacity
    # print(ht.get("line_1"))
    # print(ht.get("line_2"))
    # print(ht.get("line_3"))
    print("")
    # # # # test delete
    ht.delete("line_3")
    # ht.delete("line_2")
    ht.delete("line_1")

    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("percentage2", str(ht.load_balance_ratio())+"%")
    # Test resizing
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # # Test if data intact after resizing
    # print(ht.get("line_1"))
    # print(ht.get("line_2"))
    # print(ht.get("line_3"))

    # print("")

    # l = LinkedList()
    # l.insert("a", 1)
    # l.insert("b", 2)
    # l.insert("c", 3)
    # l.insert("d", 4)
    # print(l.head.key, l.head.value)
    # print(l.head.next.key, l.head.next.value)
    # print(l.head.next.next.key, l.head.next.next.value)
    # print(l.head.next.next.next.key, l.head.next.next.next.value)
