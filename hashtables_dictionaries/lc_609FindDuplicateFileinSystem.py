# https://leetcode.com/problems/find-duplicate-file-in-system/description

import os
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_info = defaultdict(list)
        for filepath in paths:
            directory = filepath.split(" ")[0]
            for files in filepath.split(" ")[1:]:
                # 1.txt(abcd)
                file, content = files.split("(")
                content.replace(")","")
                content_info[content].append(os.path.join(directory, file))
        result = []
        for k, v in content_info.items():
            if len(v) >= 2: # at least two files
                result.append(v)
        del content_info
        return result