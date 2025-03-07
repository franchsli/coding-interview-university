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


class Queue:
    def __init__(self):
        self.items = [None] * 100

    def enqueue(self, value):
        if not self.is_full():
            self.items = [value] + self.items[:len(self.items)-1]
        else:
            raise IndexError("The queue is full.")

    def get_first_in_index(self) -> int:
        if self.is_full():
            return len(self.items) - 1
        
        elif self.is_empty():
            raise IndexError("The queue is empty.")
        
        for i in range(len(self.items)):
            if self.items[i+1] == None:
                return i


    def deque(self):
        if not self.is_empty():
            first_in_index = self.get_first_in_index()
            temp = self.items[first_in_index]
            self.items[first_in_index] = None
            return temp
    
    def is_empty(self):
        return self.items[0] == None

    def is_full(self):
        return self.items[-1] != None