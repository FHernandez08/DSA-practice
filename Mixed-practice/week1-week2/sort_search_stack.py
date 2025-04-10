# You're building a browser history system that records each visited page (as a string) in a stack.

# Tasks
#   1. Implement the stack to record pages
#   2. Create a function to sort the stack history alphabetically
#   3. Implement binary search to check if a page exists in the sorted history

class BrowserHistory:
    def __init__(self):
        self.stack = []
    
    def push_history(self, page):
        self.stack.append(page)
    
    def get_sorted_history(self):
        return self._merge_sort(self.stack[:])
        
    def _merge_sort(self, pages):
        if len(pages) <= 1:
            return pages
        
        mid = len(pages) // 2
        left = self._merge_sort(pages[:mid])
        right = self._merge_sort(pages[mid:])
        
        return self._merge(left, right)
            
    def _merge(self, left, right):
        i, j = 0, 0
        merged_array = []
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged_array.append(left[i])
                i += 1
            else:
                merged_array.append(right[j])
                j += 1
                
        merged_array.extend(left[i:])
        merged_array.extend(right[j:])
        
        return merged_array        
    
    def search_page(self, page):
        sorted_search = self.get_sorted_history()
        return self.binary_search(sorted_search, page)
    
    def binary_search(self, arr, target):
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False
    
    
###### TESTING ######
history = BrowserHistory()
history.push_history("zebra.com")
history.push_history("apple.com")
history.push_history("openai.com")

# Test Sorted History
print(history.get_sorted_history())
# Output: ['apple.com', 'openai.com', 'zebra.com']

# Test Search
print(history.search_page("openai.com"))  # True
print(history.search_page("google.com"))  # False