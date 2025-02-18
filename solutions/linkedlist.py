from typing import Any, Union


class Node:
    def __init__(self, value: Any = None, next: Any = None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head: Node = None):
        self.head = head
        self._size: int = 0

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def set_size(self, new_size: int) -> None:
        self._size = new_size

    def is_empty(self) -> bool:
        return self.size == 0

    def value_at(self, index: int) -> Union[Any, Exception]:
        if index < 0:
            raise IndexError(
                f"The index {index} is invalid, it must be grater or equal than zero"
            )

        elif index > self.size - 1:
            raise IndexError(f"The given index is bigger than the Linked List")

        counter: int = 0
        pointer = self.head

        while counter != index and pointer.next:
            pointer = pointer.next
            counter += 1

        return pointer

    def push_front(self, value: Any) -> None:
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head
        self.set_size(self.size + 1)

    def pop_front(self) -> Union[Any, Exception]:
        if not self.is_empty():
            temp = self.head
            self.head = self.head.next
            self.set_size(self.size - 1)
            return temp.value
        
        raise Exception("The linked list is empty")
    
    def push_back(self, value: Any) -> Union[None, Exception]:
        if not self.is_empty():
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            
            pointer.next = Node(value)
            self.set_size(self.size + 1)
        
        raise Exception("The linked list is empty")
    
    def pop_back(self) -> Union[Any, Exception]:
        if not self.is_empty():

            if self.size == 1:
                temp = self.head
                self.head = None
                return temp.value

            pointer = self.head
            while pointer.next.next:
                pointer = pointer.next
                counter += 1
            
            temp = pointer.next
            pointer.next = None

            self.set_size(self.size - 1)

            return temp
                
        raise Exception("The linked list is empty")
    
    def front(self) -> Union[Any, Exception]:
        if not self.is_empty():
            return self.head.value
        else:
            raise Exception("The linked list is empty")
        
    def back(self) -> Union[Any, Exception]:
        if not self.is_empty():
            pointer = self.head
            while pointer.next:
                pointer = pointer.next 
            return pointer.value
        
        else:
            raise Exception("The linked list is empty")
    
    def insert(self, index: int, value: Any) -> Union[Any, Exception]:
        if self.is_empty():
            raise Exception("The linked list is empty")

        elif self.size < index + 1:
            raise IndexError(f"The given index is bigger than the Linked List")     

        else:
            if index == 0:
                self.push_front(value)

            elif index == self.size - 1:
                self.push_back(value)

            
            pointer = self.head
            counter = 0
            while pointer.next and counter + 1 != index:
                pointer = pointer.next
                counter += 1

            new_node = Node(value, pointer.next)
            pointer.next = new_node
            self.set_size(self.size + 1)    
  
