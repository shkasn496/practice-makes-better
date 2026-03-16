# https://leetcode.com/problems/number-of-provinces/description/?envType=company&envId=facebook&favoriteSlug=facebook-six-months
"""
Solution 1: DFS
TC: O(n2)
SC: O(n)
"""
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces = 0
        def dfs(city):
            if city in visited:
                return 0
            visited.add(city)
            cities = 1
            for ngbr, state in enumerate(isConnected[city]):
                if ngbr == city or state == 0: continue
                cities += dfs(ngbr)
            return cities
        for city in range(n):
            if city not in visited:
                if dfs(city) >= 1:
                    provinces += 1
        del visited
        return provinces
                