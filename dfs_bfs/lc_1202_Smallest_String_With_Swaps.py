# https://leetcode.com/problems/smallest-string-with-swaps/description/
"""
Solution 1: DFS - Connected components can be sorted to least values
            Create an adjacency graph of index connections that can perform swap
            Visit the index paths that are connected and store the indexes
            Get the characters along the index paths
            Sort the chars array and the index array
            Add sorted chars in the right index in the result array
Runtime 844 ms Beats 14.48%
Memory 100.2 MB Beats 5.18%

TC: O(E) + O(VlogV) 
SC: O(E+V)
"""
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        graph = {i:set() for i in range(len(s))}
        for i, j in pairs:
            graph[i].add(j)
            graph[j].add(i)
        visited = set()
        result = list(s)
        def dfs(idx, indexes):
            visited.add(idx)
            indexes.append(idx)
            for ngbr in graph[idx]:
                if ngbr not in visited:
                    dfs(ngbr, indexes)
            return
        for idx in range(len(s)):
            if idx not in visited:
                indexes = []
                dfs(idx, indexes)
                indexes.sort()
                chars = sorted([s[i] for i in indexes])
                for i, c in zip(indexes, chars):
                    result[i]=c
        del graph, visited
        return "".join(result)