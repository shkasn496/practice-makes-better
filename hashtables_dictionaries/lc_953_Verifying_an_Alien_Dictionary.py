# https://leetcode.com/problems/verifying-an-alien-dictionary/
"""
Solution 1: Use a hashmap to store the indexes of the characters in the order.
Runtime 39 ms Beats 96.53%
Memory 16.2 MB Beats 93.14%

TC: O(m) where we go through all the letters in the words.
SC:O(1) because the hashmap will store only 26 chars which would be considered a 
constant.
"""
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words)==1:return True
        priority = {order[i]: i for i in range(len(order))}
        for i in range(0,len(words)-1):
            word1, word2 = words[i], words[i+1]
            for j in range(len(word1)):
                if j >= len(word2) or priority[word1[j]]>priority[word2[j]]:
                    del priority
                    return False
                if word1[j]==word2[j]:continue
                if priority[word1[j]]<priority[word2[j]]: break
        del priority
        return True