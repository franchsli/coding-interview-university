from linkedlist import LinkedList
from dataclasses import dataclass

@dataclass
class Queue(LinkedList):

    def enqueue(self, value):
        self.push_front(value)
    
    def deque(self):
        return self.pop_back()
    
    def empty(self):
        return self.is_empty()
    
# fixed-size array implementation

@dataclass
class Queue:
    items = [None] * 100

    def enqueue(self, value):
        self.push_front(value)
    
    def deque(self):
        self.pop_back()
    
    def empty(self):
        return self.is_empty()

    def full(self):
        pass