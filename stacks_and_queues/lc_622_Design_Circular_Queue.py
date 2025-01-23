# https://leetcode.com/problems/design-circular-queue/description/
"""
Solution 1: Use Doubly-LL

"""
class Node:
    def __init__(self, val: int, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int): # TC -> O(1)
        self.k = k
        self.left = Node(val=0)
        self.right = Node(val=0)
        self.left.next = self.right
        self.right.prev = self.left
        self.nodes = 0

    def enQueue(self, value: int) -> bool: # TC -> O(1)
        if self.isFull(): return False
        node = Node(val = value)
        temp = self.right.prev
        self.right.prev = node
        temp.next = node
        node.next = self.right
        node.prev = temp
        self.nodes += 1
        return True
        
    def deQueue(self) -> bool: # TC -> O(1)
        if self.isEmpty(): return False
        node = self.left.next
        self.left = self.left.next
        self.nodes -= 1
        del node
        return True

    def Front(self) -> int: # TC -> O(1)
        if self.isEmpty(): return -1
        return self.left.next.val

    def Rear(self) -> int: # TC -> O(1)
        if self.isEmpty(): return -1
        return self.right.prev.val

    def isEmpty(self) -> bool: # TC -> O(1)
        return self.nodes == 0

    def isFull(self) -> bool: # TC -> O(1)
        return self.nodes==self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()