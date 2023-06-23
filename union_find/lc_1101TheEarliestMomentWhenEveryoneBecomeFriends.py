# https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/description/
"""
SOlution : Using Unionfind datastructure
Runtime 103 ms Beats 99.21%
Memory 14.2 MB Beats 72.84%

TC: O(nlog(n))+O(n)+O(m*A(n))
SC: O(n)+O(m)
"""
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        if n==2:return logs[0][0]
        if len(logs)<n-1:return -1 #no time to make all friends
        logs.sort(key=lambda x:x[0]) #sort based on timestamp
        # initially, treat every friend as it's own group
        group_count = n
        uf = UnionFind(n)
        for ts, friend_a, friend_b in logs:
            if uf.union(friend_a, friend_b):
                group_count-=1
            # moment when all individuals are connected
            if group_count == 1:
                del uf
                return ts
        # There are still more than one groups left,
        #  i.e. not everyone is connected.
        del uf
        return -1
class UnionFind():
    def __init__(self, size):
        self.parent = {i:i for i in range(size)}
        self.rank = [0]*size
        return
    def find(self, x):
        if self.parent[x]==x:return x
        return self.find(self.parent[x])
    def union(self, x, y):
        parent_x, parent_y = self.find(x), self.find(y)
        if parent_x==parent_y:return False
        elif self.rank[parent_x]>self.rank[parent_y]:
            self.parent[parent_y]=parent_x
            self.rank[parent_x]+=1
        else:
            self.parent[parent_x]=parent_y
            self.rank[parent_y]+=1
        return True

"""
Solution 2: Using Graph and set 
Runtime 124 ms Beats 81.67%
Memory 14.1 MB Beats 96.65%

TC: O(M log M + M*N)
SC: O(M + N)
"""
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        if n==2:return logs[0][0]
        if len(logs)<n-1:return -1 #no time to make all friends
        logs.sort(key=lambda x:x[0]) #sort based on timestamp
        graph = {i:set() for i in range(n)}
        for i in range(n): graph[i].add(i) # initialize node val in graph
        for ts, friend_a, friend_b in logs:
            l1, l2 = len(graph[friend_a]), len(graph[friend_b])
            if l1>=l2:
                graph[friend_a]=graph[friend_a].union(graph[friend_b])
            else:
                graph[friend_b]=graph[friend_b].union(graph[friend_a])
                friend_a=friend_b
            
            for friend in graph[friend_a]:
                graph[friend]=graph[friend_a]
            if len(graph[friend_a])==n:return ts
        return -1