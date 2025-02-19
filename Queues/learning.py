from collections import deque

class Queue:
    def __init__(self):
        self._data = deque()
        
    def enqueue(self, item):
        self._data.append(item)
        
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        return self._data.popleft()
    
    def is_empty(self):
        return not self._data
    
    def size(self):
        return len(self._data)
    
    def peek(self):
        if self.is_empty():
           raise IndexError("Can't peek from an empty queue")
        return self._data[0]