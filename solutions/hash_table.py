class HashTable:
    def __init__(self):
        self.table = [None] * 100
    
    def hash(self, key) -> int:
        return hash(key) % len(self.table)
    
    def add(self, key, value) -> None:
        storage_index = self.hash(key)
        storage_index_value = self.table[storage_index]
        if storage_index_value == None:
            self.table[storage_index] = value
        elif type(storage_index_value) == list:
            self.table[storage_index] = self.table[storage_index] + [value]
        else:
            temp = [storage_index_value, value]
            self.table[storage_index] = temp
            del temp
    
    def exists(self, key) -> bool:
        return self.table[self.hash(key)] != None