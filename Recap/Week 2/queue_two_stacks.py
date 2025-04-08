# Implement a queue using two stacks
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self, item):
        self.stack1.append(item)
        
    def dequeue(self):
        if self.stack2:
            return self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        

# Test case
q = MyQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # Expected: 1
print(q.dequeue())  # Expected: 2
q.enqueue(4)
print(q.dequeue())  # Expected: 3
print(q.dequeue())  # Expected: 4