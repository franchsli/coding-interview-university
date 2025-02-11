
class Array:
    def __init__(self, *items) -> None:
        self.items = []
        self.size = 0
        self.populate(items)
    
    def populate(self, items) -> None:
        for item in items:
            self.push(item)

    def capacity(self) -> int:
        return 512

    def is_empty(self) -> bool:
        return self.size > 0

    def at(self, index: int):
        if index > 1023:
            raise IndexError("Index is out of array length limit, the limit is 1024 items")
        elif index > self.size - 1:
            raise IndexError(f"Index is out of array current length, there are {self.size} items")
        else:
            return self.items[index]
    
    def print_items(self) -> None:
        for i in range(self.size):
            print(self.at(i))

    def push(self, item) -> None:
        self.items += [item]
        self.size += 1
    
    def insert(self, item, index) -> None:
        if index > self.size - 1:
            raise IndexError(f"Index is out of array current length, there are {self.size} items")
        elif index == self.size:
            self.push(item)
        elif index < 0:
            self.prepend(item)
        else:
            pass

    
    def prepend(self, item) -> None:
        self.items = [item] + self.items


test = Array(1,2,3,4,5)
test.print_items()