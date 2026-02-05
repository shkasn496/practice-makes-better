# https://leetcode.com/problems/valid-word-abbreviation/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
"""
Solution:
TC: O(n) n = len(abbr)
SC: O(1)
"""
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        num = 0
        i = 0
        for c in abbr:
            if c.isnumeric():
                # check leading zero
                if int(c) == 0 and num==0: return False
                num = num * 10 + int(c)
            else:
                # check if char abbr
                if num:
                    i+=num # increment i pointer
                    num = 0 # reset num
                if i >= len(word): return False
                if c != word[i]: return False
                i += 1 # check next char
        if num:
            i += num
            num = 0
        return i == len(word)