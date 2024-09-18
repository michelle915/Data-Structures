# hash_map.py
# ===================================================
#
# Implement a hash map with chaining
# ===================================================
class SLNode:
    def __init__(self, key, value):
        self.next = None
        self.key = key
        self.value = value
    def __str__(self):
        return '(' + str(self.key) + ', ' + str(self.value) + ')'

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def add_front(self, key, value):
        """Create a new node and inserts it at the front of the linked list
        Args:
        key: the key for the new node
        value: the value for the new node"""
        new_node = SLNode(key, value)
        new_node.next = self.head
        self.head = new_node
        self.size = self.size + 1
    def remove(self, key):
        """Removes node from linked list
        Args:
        key: key of the node to remove """
        if self.head is None:
        return False
        if self.head.key == key:
        self.head = self.head.next
        self.size = self.size - 1
        return True
        node = self.head
        while node.next is not None:
        # remove if found
        if node.next.key == key:
        node.next = node.next.next
        self.size = self.size - 1
        return True
        node = node.next
        # not found in list
        return False
    def contains(self, key):
        """Searches linked list for a node with a given key
        Args:
        key: key of node
        Return:
        node with matching key, otherwise None"""
        if self.head is not None:
            cur = self.head
        while cur is not None:
            if cur.key == key:
                return cur
        cur = cur.next
        return None

    def __str__(self):
        out = '['
        if self.head is not None:
        cur = self.head
        out = out + str(self.head)
        cur = cur.next
        while cur is not None:
        out = out + ' -> ' + str(cur)
        cur = cur.next
        out = out + ']'
        return out
        def hash_function_1(key):
        hash = 0
        for i in key:
        hash = hash + ord(i)
        return hash
    def hash_function_2(key):
        hash = 0
        index = 0
        for i in key:
        hash = hash + (index + 1) * ord(i)
        index = index + 1
        return hash
class HashMap:
        def __init__(self, capacity, function):
        """
        Creates a new hash map with the specified number of buckets.
        Args:
        capacity: the total number of buckets to be created in the hash table
        function: the hash function to use for hashing values
        """
        self._buckets = []
        for i in range(capacity):
        self._buckets.append(LinkedList())
        self.capacity = capacity
        self._hash_function = function
        self.size = 0
def clear(self):
        """
        Empties out the hash table deleting all links in the hash table.
        """
        # reset the buckets in the hash table
        self._buckets = []
        for i in range(self.capacity):
        self._buckets.append(LinkedList())
        self.size = 0

def get(self, key):
        """
        Returns the value with the given key.
        Args:
        key: the value of the key to look for
        Return:
        The value associated to the key. None if the link isn't found.
        """
        # get the index/bucket of the hash table for the given key
        index = self._hash_function(key) % self.capacity
        bucket = self._buckets[index]
        # if the bucket is empty, return None
        if bucket is None:
        return None
        # save result of contains; is either the found node or None
        node = bucket.contains(key)
        if node is None:
        return None
        # if the bucket contains the key, return the value associated with the key
        return node.value

def resize_table(self, capacity):
"""
Resizes the hash table to have a number of buckets equal to the given
capacity. All links need to be rehashed in this function after resizing
Args:
capacity: the new number of buckets.
"""
# create a temporary hashMap with the given capacity
temp = HashMap(capacity, self._hash_function)
# iterate over the buckets in the existing hash table, calculate index for
keys_and_values = DynamicArray()

for bucket in range(self._buckets.length()):
    if self._buckets[bucket].length() != 0:
        for node in self._buckets[bucket]:
            keys_and_values.append((node.key, node.value))

# and put the key and value in the temporary hashMap
index = 0
while index < keys_and_values.length():
    key_value = keys_and_values[index]
    (key, value) = key_value
    temp.put(key, value)
    index += 1

# point the existing hashMap to the temporary hashMap and change capacity
self._buckets = temp._buckets
self._capacity = capacity