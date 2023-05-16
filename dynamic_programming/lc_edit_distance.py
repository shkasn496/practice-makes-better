# https://leetcode.com/problems/edit-distance/description/
"""
Solution 1: dfs+memoization
Runtime 90 ms Beats 89.72% 
Memory 18.8 MB  Beats 21.16%
TC:O(m*n)
SC:O(m*n)+O(m+n) for recursive stack
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M, N = len(word1), len(word2)
        cache={}
        def recurse(i, j):
            if i<0 or j<0:return max(i,j)+1
            if (i,j) not in cache:
                curr_op = 0
                if word1[i]==word2[j]:curr_op+=recurse(i-1,j-1)
                else:
                    min_ops = min( \
                    min(recurse(i,j-1), recurse(i-1,j)),\
                     recurse(i-1,j-1))
                    curr_op+=min_ops+1
                cache[(i,j)]=curr_op
            return cache[(i,j)]
        min_operations = recurse(M-1,N-1)
        del cache
        return min_operations


"""
Solution 2: Dynamic Programming Tabularization
TC:O(m*n)
SC:O(m*n)
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1), len(word2)
        if m==0 or n==0:return max(m,n)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):dp[i][0]=i
        for j in range(n+1):dp[0][j]=j
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=1+min( \
                        dp[i-1][j-1], \
                        min(dp[i-1][j], dp[i][j-1]))
        min_operations = dp[m][n]
        del dp
        return min_operations

"""
Solution 3: Best space optimization on Tabularization method

TC:O(m*n)
SC:O(m)
"""
