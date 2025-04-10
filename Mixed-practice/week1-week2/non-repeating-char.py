# Given a stream of lowercase characters, for each character, return the first non-repeating character in the stream so far. If there is none, return '_'.
from collections import deque

class FirstNonRepeating:
    def __init__(self):
        self.queue = deque()
        
    def add_char(self, char):
        pass
    
    def get_first_non_repeating(self):
        pass