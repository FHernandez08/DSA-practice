class queue_stack:
    def __init__(self):
        self.inner_stack = []
        self.outer_stack = []
        
    def enqueue(self, item):
        self.inner_stack.append(item)
        
    def dequeue(self):
        if not self.outer_stack:
            while self.inner_stack:
                self.outer_stack.append(self.inner_stack.pop())
        
        if not self.outer_stack:
            print("The queue is empty.")
            return None
        
        return self.outer_stack.pop()
    
    def peek(self):
        if not self.outer_stack:
            while self.inner_stack:
                self.outer_stack.append(self.inner_stack.pop())
                
        if not self.outer_stack:
            print("The queue is empty!")
            return None
        
        return self.outer_stack[-1]
    
    def is_empty(self):
        if not self.outer_stack and not self.inner_stack:
            return True
        return False
    

#### TESTS ####
# Test 1
queue = queue_stack()

# The queue should be empty when initialized
assert queue.is_empty() == True, "Test Case 1 Failed: Queue should be empty initially."
print("Test Case 1 Passed: Queue is empty after initialization.")

# Test 2
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# The queue should not be empty now
assert queue.is_empty() == False, "Test Case 2 Failed: Queue should not be empty after enqueuing elements."
print("Test Case 2 Passed: Queue is not empty after enqueuing.")

# Test 3
# Peek should return the front element (1 in this case) without removing it
assert queue.peek() == 1, "Test Case 3 Failed: Peek should return the front element."
print("Test Case 3 Passed: Peek returns the correct front element.")

# Test 4
# Dequeue and check if elements are dequeued correctly
assert queue.dequeue() == 1, "Test Case 4 Failed: Dequeue should return 1."
assert queue.dequeue() == 2, "Test Case 4 Failed: Dequeue should return 2."
assert queue.dequeue() == 3, "Test Case 4 Failed: Dequeue should return 3."
print("Test Case 4 Passed: Dequeue removes elements in correct order.")

# Test 5
# The queue should be empty after all elements are dequeued
assert queue.is_empty() == True, "Test Case 5 Failed: Queue should be empty after dequeuing all elements."
print("Test Case 5 Passed: Queue is empty after dequeuing all elements.")

# Test 6
# Peek on an empty queue should return None and print the empty message
assert queue.peek() == None, "Test Case 6 Failed: Peek should return None on an empty queue."
print("Test Case 6 Passed: Peek on empty queue returns None.")

# Test 7
# Dequeue on an empty queue should return None and print the empty message
assert queue.dequeue() == None, "Test Case 7 Failed: Dequeue should return None on an empty queue."
print("Test Case 7 Passed: Dequeue on empty queue returns None.")
