class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = []
        self.values = []

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        if key in self.keys:
            i = self.keys.index(key)
            self.values[i] = value
        else:
            self.keys.append(key)
            self.values.append(value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key in self.keys:
            i = self.keys.index(key)
            return self.values[i]
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.keys:
            i = self.keys.index(key)
            del(self.values[i])
            del(self.keys[i])

h = MyHashMap()

print(h.put(1,1))
print(h.put(2,2))
print(h.get(1))
print(h.remove(2))
print(h.get(2))
print(h.get(1))
