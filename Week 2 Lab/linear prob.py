class HashTableLinear:
    def __init__(self, size=7919, a=33):
        self.table_size = size
        self.count = 0
        self.a = a
        self.array = build_array(self.table_size)

    def __len__(self):
        return self.count

    def _hash_value(self, key): # should be private
        h = 0
        for i in range(len(key)):
            h = (h*self.a + ord(key[i])) % self.table_size

    def insert(self, key, value):
        position = self._hash_value(key)
        for i in range(self.table_size):
            if self.array[position] is None:
                self.array[position] = (key, value)
                self.count += 1
                return

            if self.array[position][0] == key:
                self.array[position] = (key, value)
            else:
                position += 1
                if position >= self.table_size:
                    position = 0
