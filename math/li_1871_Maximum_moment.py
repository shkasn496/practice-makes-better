# https://www.lintcode.com/problem/1871/description?_from=problem_tag&fromId=63
"""
Solution:
66 ms
time cost
·
4.97 MB
memory cost
·
Your submission beats
91.58 % Submissions

TC:SC:O(1)
"""
class Solution:
    """
    @param time: a string of Time
    @return: The MaximumMoment
    """
    def maximum_moment(self, time: str) -> str:
        # Write your code here.
        H, M, _, S1, S2 = time
        if H=='?':
            if M=='?' or int(M)<=3:H='2'
            else:H='1'
        if M=='?':
            if H=='2':M='3'
            else:M='9'
        if S1=='?':S1='5'
        if S2=='?':S2='9'
        return f"{H}{M}:{S1}{S2}"