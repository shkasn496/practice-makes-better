# https://leetcode.com/problems/two-sum-iii-data-structure-design/

class TwoSum:

    def __init__(self):
        self.count = collections.defaultdict(int)

    def add(self, number: int) -> None:
        self.count[number] += 1

    def find(self, value: int) -> bool:
        if not self.count: return False
        for num1 in self.count.keys():
            num2 = value - num1
            if num2 == num1 and self.count[num2] >= 2:
                return True
            elif num2 in self.count and num1 != num2 and self.count[num2] >= 1:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)