# https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/
"""
Solution 1: Brute Force (not great, but works)
Runtime 779 ms Beats 10.37%
Memory 19 MB Beats 12.4%
TC:O(m*n)^2
SC:O(1)
"""
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        square_count=0
        def check_sub_square(r,c,square_side):
            for r1 in range(r,r+square_side):
                for c1 in range(c,c+square_side):
                    if matrix[r1][c1]==0:return False
            return True
        for r in range(m):
            for c in range(n):
                if matrix[r][c]==0:continue
                r1, c1 = 0,0
                while r+r1 <m and matrix[r+r1][c]==1:r1+=1
                while c+c1 <n and matrix[r][c+c1]==1:c1+=1
                square_side = min(r1, c1)
                
                while square_side:
                    if check_sub_square(r,c,square_side):
                        square_count+=square_side
                        break
                    square_side-=1
        return square_count

"""
Solution 2: Dynamic Programming Tabularization approach
Runtime 600 ms Beats 53.89%
Memory 18.8 MB Beats 18.70%
TC:O(m*n)
SC:O(m*n)
"""
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        square_count=0
        def check_sub_square(r,c,square_side):
            for r1 in range(r,r+square_side):
                for c1 in range(c,c+square_side):
                    if matrix[r1][c1]==0:return False
            return True
        for r in range(m):
            for c in range(n):
                if matrix[r][c]==0:continue
                r1, c1 = 0,0
                while r+r1 <m and matrix[r+r1][c]==1:r1+=1
                while c+c1 <n and matrix[r][c+c1]==1:c1+=1
                square_side = min(r1, c1)
                
                while square_side:
                    if check_sub_square(r,c,square_side):
                        square_count+=square_side
                        break
                    square_side-=1
        return square_count


"""
Solution 3: Best space optimized DP tabularization approach
Runtime 571 ms Beats 90.18%
Memory 18.8 MB Beats 18.70%

TC:O(m*n)
SC:O(n)
"""
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        prev_row = [matrix[0][c] for c in range(n)]
        square_count=sum(prev_row)         
        for r in range(1,m):
            current_row=[0]*n
            for c in range(n):
                if c==0:
                    current_row[c] =matrix[r][c]
                    square_count+=current_row[c]
                    continue
                if matrix[r][c]==0:continue
                min_ngbr=min(min(prev_row[c], prev_row[c-1]), current_row[c-1])
                current_row[c]=min_ngbr+matrix[r][c]
                square_count+=current_row[c]
            prev_row=current_row
        del prev_row
        return square_count

"""
Solution 4: Even better approach is to leverage to matrix to store
            DP counts (BEST APPROACH AS NO NEW MEMORY IS USED)
Runtime 539 ms Beats 99.44%
Memory 18.9 MB Beats 18.70%
TC:O(m*n)
SC:O(1)
"""
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        square_count = 0
        for col in range(n):
            square_count += matrix[0][col]
        for row in range(1,m):
            square_count+=matrix[row][0]
        for row in range(1,m):
            for col in range(1,n):
                if matrix[row][col]==1 and matrix[row-1][col]>0 \
                and matrix[row][col-1] > 0 and matrix[row-1][col-1] > 0:
                    matrix[row][col]+= min(matrix[row-1][col],\
                     matrix[row][col-1],matrix[row-1][col-1])
                square_count+=matrix[row][col]
        del matrix
        return square_count