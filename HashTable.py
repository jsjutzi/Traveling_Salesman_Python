class HashTableEntry:
    def __init__(self, key, item):
        self.key = key
        self.item = item


class HashMap:
    def __init__(self, initial_capacity=10):
        self.map = []
        for i in range(initial_capacity):
            self.map.append([])

    # Generate Hash Key -- O(1)
    def generate_hash_key(self, key):
        return int(key) % len(self.map)

    # Get value from hash table -- O(n)
    def get_value(self, key):
        hash_key = self.generate_hash_key(key)
        if self.map[hash_key] is not None:
            for values in self.map[hash_key]:
                if values[0] == key:
                    return values[1]
        return None

    # Insert new value to hash table -- O(n)
    def insert(self, key, value):
        hash_key = self.generate_hash_key(key)
        hash_value = [key, value]

        if self.map[hash_key] is None:
            self.map[hash_key].append(hash_value)
            return True
        else:
            for values in self.map[hash_key]:
                if values[0] == key:
                    values[1] = value
                    return True

            self.map[hash_key].append(hash_value)
            return True

    # Update existing value in hash table -- O(n)
    def update(self, key, value):
        hash_key = self.generate_hash_key(key)
        if self.map[hash_key] is not None:
            for values in self.map[hash_key]:
                if values[0] == key:
                    values[1] = value
                    return True
        else:
            print("There was no matching record to update")


