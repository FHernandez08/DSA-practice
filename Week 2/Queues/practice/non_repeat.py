from collections import deque

def non_repeat_chars(array):
    curr_queue = deque()
    hash_map = {}

    for char in array:
        curr_queue.append(char)

        if char not in hash_map:
            hash_map[char] = 1
        else:
            hash_map[char] += 1

        while curr_queue and hash_map[curr_queue[0]] > 1:
            curr_queue.popleft()

        if curr_queue:
            print(curr_queue[0], end=" ")
        else:
            print("None", end=" ")


non_repeat_chars("abcabc")
non_repeat_chars("aabbc")
non_repeat_chars("abcd")
non_repeat_chars("aabb")
