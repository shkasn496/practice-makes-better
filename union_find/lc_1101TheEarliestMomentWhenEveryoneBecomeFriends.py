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
        uf = UnionFind(n)
        groups=n
        for timestamp, friend_a, friend_b in logs:
            if uf.union(friend_a, friend_b):groups-=1
            if groups==1:return timestamp
        return -1

class UnionFind(object):
    def __init__(self, size) -> None:
        self.groups = {i:i for i in range(size)}#key:node, value:parent of node
        self.rank = [0]*size
        return
    def find(self, x):
        if self.groups[x]==x:
            return x
        return self.find(self.groups[x])
    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)
        if parent_x==parent_y:#already in same group
            return False
        # Merge the lower-rank group into the higher-rank group.
        if self.rank[parent_x]>self.rank[parent_y]:
            self.groups[parent_y]=parent_x
        elif self.rank[parent_x]<self.rank[parent_y]:
            self.groups[parent_x]=parent_y
        else:
            self.groups[parent_y]=parent_x
            self.rank[parent_x]+=1
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