# https://leetcode.com/problems/word-ladder/description/
"""
Solution: BFS
TC: O(n^2)
SC: O(n^2)
"""
from queue import Queue
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = {w for w in wordList}
        if endWord not in words: return 0
        queue = Queue()
        queue.put((beginWord, 1))
        visited = set()
        while not queue.empty():
            word, count = queue.get()
            if word == endWord: return count
            visited.add(word)
            for c in range(len(beginWord)):
                for i in range(ord('a'), ord('z')+1):
                    new_word = word[:c]+chr(i)+word[c+1:]
                    if new_word in visited or new_word not in words:
                        continue
                    queue.put((new_word, count + 1))
        del queue, words, visited
        return 0