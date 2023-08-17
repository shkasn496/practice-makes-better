# https://leetcode.com/problems/remove-invalid-parentheses/description/
"""
Solution 1: Backtracking - Slow solution as it checks all cases.
            Caching the previously created strings didnt give a significant performance gain.

Runtime 2349 ms Beats 15.52%
Memory 16.3 MB Beats 90.85%

TC: O(2^N)
SC:O(N)
"""
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if len(s)==1:return [""] if not s[0].isalpha() else [s]
        longest_string = -1
        result = set()
        def backtrack(idx, open_b, close_b, curr_string):
            nonlocal longest_string, result
            # 1. Conditions
            if idx > len(s) or open_b < close_b:return
            # 2. Goal
            if idx==len(s):
                if open_b == close_b:
                    # check if less removals happened in curr string to make it valid
                    if len(curr_string) > longest_string:
                        # reset our existing result
                        result = set()
                        result.add("".join(curr_string))
                        longest_string = len(curr_string)
                    elif len(curr_string) == longest_string:
                        result.add("".join(curr_string))
                return
            # 3. Choices: Keep bracket or remove bracket
            curr_char = s[idx]
            if curr_char == '(':
                # Choice 1: Keep the opening bracket
                backtrack(idx+1, open_b+1, close_b, curr_string + [s[idx]])
                # Choice 2 : Remove the opening bracket
                backtrack(idx+1, open_b, close_b, curr_string)
            elif curr_char == ')':
                # Choice 1: Keep the closing bracket, can be done only if open_b > close_b
                if open_b > close_b:
                    backtrack(idx+1, open_b, close_b+1, curr_string + [s[idx]])
                # Choice 2 : Remove the closing bracket
                backtrack(idx+1, open_b, close_b, curr_string)
            else: backtrack(idx+1, open_b, close_b, curr_string + [s[idx]]) # add alpha char
            return
        backtrack(0, 0, 0, [])
        return result

"""
Solution 2: One way to reduce the no. of graphs is to know the min no of invalid parentheses present in the string.
            To find that, use a open_remain and close_remain counts to 
            find open and close brackets that arent natched.
            Then, in the choices of backtracking :
                for open brackets, only remove them if open_remain count is greater than zero.
                for close brackets, only remove them if close_remain count is greater than zero.

Runtime 1707 ms Beats 31.70%
Memory 16.4 MB Beats 77.12%              

TC: O(n) + O(2^N)
SC:O(n)
"""
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if len(s)==1:return [""] if not s[0].isalpha() else [s]
        result = set()
        def check_invalid_parentheses_count(s):
            open_remain, close_remain  = 0, 0
            for c in s:
                if c.isalpha():continue
                elif c=='(': open_remain+=1
                else:
                    if open_remain:open_remain-=1
                    else: close_remain+=1
            return open_remain, close_remain

        open_remain, close_remain = check_invalid_parentheses_count(s)

        def backtrack(idx, open_b, close_b, curr_string, open_remain, close_remain):
            # 1. Conditions
            if idx > len(s) or open_b < close_b:return
            # 2. Goal
            if idx==len(s):
                if open_b == close_b and open_remain==close_remain==0:
                    result.add("".join(curr_string))
                return
            # 3. Choices: Keep bracket or remove bracket
            curr_char = s[idx]
            if curr_char == '(':
                # Choice 1: Keep the opening bracket
                backtrack(idx+1, open_b+1, close_b, curr_string + [s[idx]], \
                open_remain, close_remain)
                # Choice 2 : Remove the opening bracket only if open_remain > 0
                if open_remain > 0: 
                    backtrack(idx+1, open_b, close_b, curr_string, open_remain-1, close_remain)
            elif curr_char == ')':
                # Choice 1: Keep the closing bracket, can be done only if open_b > close_b
                if open_b > close_b:
                    backtrack(idx+1, open_b, close_b+1, curr_string + [s[idx]], open_remain, close_remain)
                # Choice 2 : Remove the closing bracket only if close_remain > 0
                if close_remain > 0: 
                    backtrack(idx+1, open_b, close_b, curr_string, open_remain, close_remain - 1)
            else: 
                backtrack(idx+1, open_b, close_b, curr_string + [s[idx]], \
                 open_remain, close_remain) # add alpha char
            return
        backtrack(0, 0, 0, [], open_remain, close_remain)
        return result

"""
Solution 3: Fastest solution!!
            Only remove elements from the string one at a time if its a bracket.
            Perform a recursive loop starting from the main input string and providing
            total min_invalid_remain.
            Also using a visited sets to store visited strings that dont need to be revisited.

Runtime 120 ms Beats 80.15%
Memory 17.2 MB Beats 23.20%

TC:O(n) + O(2^N)
SC:O(n)
"""
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if len(s)==1:return [""] if not s[0].isalpha() else [s]

        def check_invalid_parentheses_count(s):
            open_remain, close_remain  = 0, 0
            for c in s:
                if c.isalpha():continue
                elif c=='(': open_remain+=1
                else:
                    if open_remain:open_remain-=1
                    else: close_remain+=1
            return open_remain, close_remain
        open_remain, close_remain = check_invalid_parentheses_count(s)

        result = set()
        visited_strings = set()

        def backtrack(curr_string, min_invalid_remain):
            # 1. Conditions
            if curr_string in visited_strings:return
            visited_strings.add(curr_string)
            # 2. Goal
            if min_invalid_remain==0: # all min invalid chars are removed
                curr_open, curr_close = check_invalid_parentheses_count(curr_string)
                # check if curr_string is also valid
                if curr_open==curr_close==0: result.add(curr_string)
                return
            # 3. Choice: only remove brackets as we are reducing all min invalid chars from main string
            for i in range(len(curr_string)):
                if curr_string[i].isalpha(): # no remove choice
                    backtrack(curr_string, min_invalid_remain)
                else:
                    backtrack( curr_string[:i]+curr_string[i+1:], min_invalid_remain-1)
            return

        backtrack(s, open_remain + close_remain)
        del visited_strings
        return result