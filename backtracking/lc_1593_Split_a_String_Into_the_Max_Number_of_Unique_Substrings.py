# https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/description/

"""Solution 1: Backtracking
Runtime 125 ms Beats 88.58%
Memory 17.62 MB Beats 91.59%

TC: O(n^2 x 2^N) 
    The O(n^2) factor accounts for the cost of generating substrings within each partition, and
    O(2^N) factor represents the exponential number of partitioning combinations.
SC: O(N) for recursive stack + max set size
"""
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        max_substring, N  = 1, len(s)
        def backtrack(i, substrings):
            nonlocal max_substring
            # Goal
            if i == N:
                max_substring = max(len(substrings), max_substring)
                return
            # Choices
            for j in range(i+1, N+1):
                substr = s[i:j]
                if substr not in substrings:
                    substrings.add(substr)
                    backtrack(j, substrings)
                    substrings.remove(substr)
            return
        backtrack(0, set())
        return max_substring


"""
Solution 2: Backtracking + Pruning 
            Pruning here is when the current count of substring will not exceed max_substring, so we shouldnt 
            continue the state tree path

Runtime 5 ms Beats 99.57% 
Memory 17.99 MB Beats 21.55%

TC: O(n^2 x 2^N) 
    The O(n^2) factor accounts for the cost of generating substrings within each partition, and
    O(2^N) factor represents the exponential number of partitioning combinations.
SC: O(N) for recursive stack + max set size
"""
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        max_substring, N  = 1, len(s)
        def backtrack(start_idx, seen, count):
            nonlocal max_substring
            # 1. Pruning Condition
            if count + N - start_idx <= max_substring:
                return
            # 2. Goal
            if start_idx == N:
                max_substring = max(count, max_substring)
                return
            # 3. choices
            for end_idx in range(start_idx+1, N+1):
                substr = s[start_idx : end_idx]
                if substr not in seen:
                    seen.add(substr)
                    backtrack(end_idx, seen, count + 1)
                    seen.remove(substr)
            return
        backtrack(0, set(), 0)
        return max_substring