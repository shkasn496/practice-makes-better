# https://leetcode.com/problems/implement-stack-using-queues/description/
"""
Solution 1: Very simple implementation of using python module - Deque
Runtime 0 ms Beats 100.00%
Memory 17.88 MB Beats 39.97%
"""
from collections import deque
class MyStack:

    def __init__(self):
        self.dq = deque()

    def push(self, x: int) -> None:
        self.dq.append(x) # O(1) append right

    def pop(self) -> int:
        if self.empty(): return 0
        return self.dq.pop() # O(1) pop right

    def top(self) -> int:
        if self.empty(): return 0
        return self.dq[-1] # O(1) view right

    def empty(self) -> bool:
        return len(self.dq) == 0 # O(1)

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

"""
Solution 2: Using 1 Queue implemented in python
Runtime 0 ms Beats 100.00%
Memory 18.12 MB Beats 14.18%
"""
from queue import Queue
class MyStack:

    def __init__(self):
        self.queue = Queue()

    def push(self, x: int) -> None:
        self.queue.put(x) # O(1) append right
        return

    def pop(self) -> int: # O(n)
        if self.empty(): return 0
        queue_len = self.queue.qsize()
        while queue_len > 1:
            self.queue.put(self.queue.get())
            queue_len -= 1
        top = self.queue.get()
        queue_len = self.queue.qsize() # reset queue size
        return top

    def top(self) -> int: # O(1)
        if self.empty(): return 0
        return self.queue.queue[-1]

    def empty(self) -> bool:
        return self.queue.qsize() == 0 # O(1)

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()