class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)        
    
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return "Can't pop from an empty stack"
        
    def length(self):
        return len(self.items)
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return "Stack is empty!"
    