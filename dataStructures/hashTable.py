class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            # Ascii value for char
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        """Add key/value to HT"""
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        """Fetch value from HT"""
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        """Delete element with key"""
        h = self.get_hash(key)
        self.arr[h] = None


if __name__ == "__main__":
    myHash = HashTable()
    myHash["march 6"] = 130
    myHash["march 6"]
    print(myHash.arr)
