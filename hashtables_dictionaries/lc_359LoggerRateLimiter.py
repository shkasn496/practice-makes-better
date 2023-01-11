# https://leetcode.com/problems/logger-rate-limiter/description/
"""
Runtime 130 ms Beats 99.79%
Memory 20.8 MB Beats 86.15%
TC: O(1)
SC: O(n)
"""
class Logger:

    def __init__(self):
        self.logger = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.logger:
            prev_timestamp = self.logger[message]
            if timestamp>=prev_timestamp:
                self.logger[message]=timestamp+10
                return True
            return False
        self.logger[message]=timestamp+10
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)