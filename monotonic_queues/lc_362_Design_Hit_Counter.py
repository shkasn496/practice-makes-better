# https://leetcode.com/problems/design-hit-counter/description
""
from collections import deque
class HitCounter:

    def __init__(self):
        self.total = 0
        self.queue = deque([]) # timestamp, freq

    def hit(self, timestamp: int) -> None:
        self.total += 1
        if not self.queue or self.queue[-1][0] != timestamp:
            self.queue.append([timestamp, 1])
        else:
            self.queue[-1][1] += 1
        return

    def getHits(self, timestamp: int) -> int:
        while self.queue and (timestamp - self.queue[0][0] >= 300):
            _, freq = self.queue.popleft()
            self.total -= freq

        return self.total
