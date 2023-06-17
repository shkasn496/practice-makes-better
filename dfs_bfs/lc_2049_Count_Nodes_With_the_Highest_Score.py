# https://leetcode.com/problems/count-nodes-with-the-highest-score/description/
"""
Solution 1: DFS Post order traversal
        - convert the list to a graph with key=node, val= immediate children
        - dfs function will give the count of child nodes for a node
        - scores for a node = left_child_count * right_child_count * (N - 1 - sum_of_children)

Runtime 1132 ms  Beats 90%
Memory 18.8 MB Beats 52.11%
        
TC: O(n)
SC:O(n)
"""
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        N = len(parents)
        graph = {i:[] for i in range(N)}
        for i, parent in enumerate(parents):
            if i==0:continue
            graph[parent].append(i)
        scores = [0]*N
        def count_child_nodes(node):
            product, sum_child = 1, 0
            for child in graph[node]:
                child_count = count_child_nodes(child)
                product*=child_count
                sum_child+=child_count
            product *= max(1, N - 1 - sum_child)
            scores[node] = product
            return sum_child + 1
        count_child_nodes(0)
        highest_scores = scores.count(max(scores))
        del graph, scores
        return highest_scores