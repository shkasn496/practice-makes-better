# https://leetcode.com/problems/top-k-frequent-words/description/
"""
Solution 1: Using maxheap
Runtime 63 ms Beats 30.70%
Memory 16.5 MB Beats 7.47%
TC: O(n)+ k*O(logN) - O(n) for Counter
                    - O(n) for heapify
                    - k*logN for heappop operation up to k times
SC: O(n)
"""
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        max_heap = [(-count,word) for word, count in Counter(words).items()]
        heapq.heapify(max_heap)
        return [heapq.heappop(max_heap)[1] for _ in range(k)]

"""
Solution 2: Using minheap.
        Very important part is to store ascii word tuple in negative 
        order of characters in minheap to get the lexicographical ordering. 
        Need to add 501 to the tuple as the length of words is 1<=word<=500
        to avoid any errors. 

Runtime 72 ms Beats 57.34%
Memory 16.4 MB Beats 32.73%

TC: O(nlogk)
SC:O(n)
"""
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq_map = Counter(words)
        minheap = []
        result = []
        for word, freq in freq_map.items():
            ascii_word = tuple(-ord(c) for c in word) + (501,)
            heapq.heappush(minheap, (freq, ascii_word, word))
            if len(minheap)>k:heapq.heappop(minheap)
        while minheap:
            result.append(heapq.heappop(minheap)[2])
        del minheap, freq_map
        return reversed(result)