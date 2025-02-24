from dataclasses import dataclass

@dataclass
class Stack:
    items = []

    def add(self, item) -> None:
        self.items.append(item)
    
    def pop(self) -> None:
        self.items.pop()
        