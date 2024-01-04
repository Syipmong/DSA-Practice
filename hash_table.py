class HashTable:
    def __init__(self):
        """
        Initialize a hash table with a default size of 10.
        """
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        """
        Hashes the given key and returns the index in the hash table.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Inserts a key-value pair into the hash table.
        """
        index = self._hash_function(key)
        self.table[index].append((key, value))

    def get(self, key):
        """
        Retrieves the value associated with the given key from the hash table.
        Raises a KeyError if the key is not found.
        """
        index = self._hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        raise KeyError(f"Key '{key}' not found in the hash table.")

    def remove(self, key):
        """
        Removes the key-value pair associated with the given key from the hash table.
        Raises a KeyError if the key is not found.
        """
        index = self._hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return
        raise KeyError(f"Key '{key}' not found in the hash table.")


hash_1 = HashTable()

hash_1.insert("a", 1)
hash_1.insert("b", 2)
hash_1.insert("c", 3)
hash_1.insert("d", 4)
hash_1.insert("e", 5)
hash_1.insert("f", 6)
hash_1.insert("g", 7)
hash_1.insert("h", 8)
hash_1.insert("i", 9)
hash_1.insert("j", 10)
hash_1.insert("k", 11)
hash_1.insert("l", 12)
hash_1.insert("m", 13)
hash_1.insert("n", 14)
hash_1.insert("o", 15)
hash_1.insert("p", 16)
hash_1.insert("q", 17)

print(hash_1.get("a"))
print(hash_1.get("b"))
print(hash_1.get("c"))

