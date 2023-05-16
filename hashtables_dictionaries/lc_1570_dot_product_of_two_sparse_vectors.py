# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/description/
"""
Solution 1: Using hashmap to store index and values
Runtime 1620 ms Beats 98.69%
Memory 20.4 MB Beats 21.43%
TC: O(n) for creating hashmap
    O(m) for calculating dot product
SC:O(m) where m=non-zero_elems
"""
class SparseVector:
    def __init__(self, nums: List[int]):
        self.v1 = {i:num for i, num in enumerate(nums) if num}
        return

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dot_prod = 0
        for idx, num in vec.v1.items():
            if idx in self.v1:dot_prod+=(num*self.v1[idx])
        return dot_prod

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

"""
Solution 2: Using array to store non-zero elems. Then use pointers to traverse
 the two lists. Use this solution if hashmaps aren't allowed

 TC:O(n) for init
    O(m1+m2) for dot product
SC: O(m1+m2)
"""
class SparseVector:
    def __init__(self, nums: List[int]):
        self.v1 = [(i,num) for i, num in enumerate(nums) if num]
        return

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dot_prod = 0
        i, j = 0,0
        while i<len(self.v1) and j <len(vec.v1):
            if self.v1[i][0]==vec.v1[j][0]:
                dot_prod+=(self.v1[i][1]*vec.v1[j][1])
                i+=1
                j+=1
            elif self.v1[i][0]<vec.v1[j][0]:i+=1
            else:j+=1
        return dot_prod

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)