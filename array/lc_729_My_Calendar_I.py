# https://leetcode.com/problems/my-calendar-i/description/
"""
Solution1: Brute Force
Runtime 496 ms Beats 63.30%
Memory 14.7 MB Beats 93.65%

TC: O(n^2) because book() will take O(N) for each call. If there are N calls, total TC =O(N^2)
SC: O(N)
"""
class MyCalendar:

    def __init__(self):
        self.booking=[]
        return

    def book(self, start: int, end: int) -> bool:
        for s1, e1 in self.booking:
            if start>=e1 or end <=s1:continue
            if e1-start>0:return False #there is overlap
        self.booking.append((start, end))
        return True
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

"""
Solution2: Binary Search
Runtime 227 ms Beats 94.46%
Memory 14.8 MB Beats 63.57%

TC: O(n^2) because book() will take O(logN) for each call, but inserting into list will take O(N). If there are N calls, total TC =O(N^2)
SC: O(N)
"""
class MyCalendar:

    def __init__(self):
        self.booking=[]
        return

    def book(self, start: int, end: int) -> bool:
        right = len(self.booking)
        if right < 1:
            self.booking.append((start,end))
            return True
        left = 0
        while left < right:
            mid = left + (right-left)//2
            s1,e1 = self.booking[mid]
            if start < e1 and s1 < end:return False
            if start>=e1:left=mid+1
            elif end<=s1:right=mid
        self.booking.insert(left, (start, end))
        return True



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)