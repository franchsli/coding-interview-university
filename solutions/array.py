from typing import Any, Union
class Array:
    def __init__(self, *items) -> None:
        self.items = []
        self.size = 0
        self.capacity = 1024
        self.populate(items)
    
    def populate(self, items:list[Any]) -> None:
        for item in items:
            self.push(item)


    def is_empty(self) -> bool:
        return self.size > 0

    def at(self, index: int) -> Any:
        if index > self.capacity - 1:
            self._resize(self.capacity * 2)
        elif index > self.size - 1:
            raise IndexError(f"Index is out of array current length, there are {self.size} items")
        
        for item_index, item in enumerate(self.items):
            if item_index == index:
                return item
    
    def print_items(self) -> None:
        for i in range(self.size):
            print(self.at(i))

    def push(self, item:Any) -> None:
        self.items += [item]
        self.size += 1
    
    def insert(self, item:Any, index:int) -> None:
        if index > self.size - 1:
            raise IndexError(f"Index is out of array current length, there are {self.size} items")
        elif index == self.size:
            self.push(item)
        elif index <= 0:
            self.prepend(item)
        else:
            self.items =  self.items[:index] + [item] + self.items[index:]
            self.size += 1

    def prepend(self, item:Any) -> None:
        self.items = [item] + self.items
        self.size += 1

    def pop(self) -> Any:
        temp = self.items[-1]
        self.items = self.items[:self.size-1]
        self.size -= 1
        if self.size == (self.capacity // 4):
            self._resize(self.capacity // 2)
        return temp

    def delete(self, index: int) -> None:
        result = Array()
        for i, item in enumerate(self.items):
            if i != index:
                result.push(item)
        self.items = result
        self.size -= 1
        del result

    def remove(self, item: Any) -> None:
        for index, items_item in enumerate(self.items):
            if items_item == item:
                self.delete(index)
    
    def find(self, item: Any) -> int:
        for index, items_item in enumerate(self.items):
            if items_item == item:
                return index
        else:
            return -1
    
    def _resize(self, new_capacity: int) -> None:
        self.capacity = new_capacity


test = Array(1,2,3,4,5)
test.print_items()
