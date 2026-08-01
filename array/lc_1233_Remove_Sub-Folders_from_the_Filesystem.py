# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/description

"""

Solution 1: Sort then search
TC: O(nlogk + O(n))
"""
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = [folder[0]]
        for i in range(1, len(folder)):
            subfolder = result[-1]
            subfolder += "/"
            if not folder[i].startswith(subfolder):
                result.append(folder[i])
        return result