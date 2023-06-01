# https://www.lintcode.com/problem/1900/?_from=problem_tag&fromId=63
"""
Solution 1: Decode the string and perform string match

Your code cost too much memory than we expected. 
Check your space complexity. Memory limit exceeded usually 
caused by you create a 2D-array which is unnecessary.

TC: O(min(n1, n2))
SC: 
"""
class Solution:
    """
    @param gene1: a string
    @param gene2: a string
    @return: return the similarity of two gene fragments
    """
    def gene_similarity(self, gene1: str, gene2: str) -> str:
        # write your code here
        def decode_string(s):
            num, decoded = 0, []
            for c in s:
                if c.isdigit():num+=num*10+int(c)
                else:
                    decoded.append(c*num)
                    num=0
            return "".join(decoded)
        gene1 = decode_string(gene1)
        gene2 = decode_string(gene2)
        similar, total = 0,0
        n=min(len(gene1), len(gene2))
        i=0
        while i<n:
            c1 = gene1[i]
            c2 = gene2[i]
            if c1==c2:similar+=1
            total+=1
            i+=1
        del gene1, gene2
        return f"{similar}/{total}"

"""
Solution 2: Accepted solution
time cost 101 ms
memory cost 5.54 MB
Your submission beats 96.34 %
Submissions
TC: O(N)
SC:O(N)
"""
class Solution:
    """
    @param gene1: a string
    @param gene2: a string
    @return: return the similarity of two gene fragments
    """
    def gene_similarity(self, gene1: str, gene2: str) -> str:
        # write your code here
        def decode_str(s):
            num_list, char_list = [], []
            num = 0
            for c in s:
                if c.isdigit():num=num*10+int(c)
                else:
                    num_list.append(num)
                    char_list.append(c)
                    num=0
            return num_list, char_list
        num_list1, char_list1 = decode_str(gene1)
        num_list2, char_list2 = decode_str(gene2)
        #total = sum(num_list) since Guarantee the length of Gene1 and Gene2 by expansion are equal.
        similar, total = 0, sum(num_list1)
        if sum(num_list1) != sum(num_list2) or len(num_list1)!=len(char_list1)\
        or len(num_list2)!=len(char_list2):return f"{similar}/{total}"
        i, j = 0,0
        while i<len(num_list1) and j<len(num_list2):
            c1, c2 = char_list1[i], char_list2[j]
            if num_list1[i] == num_list2[j]:
                if c1==c2:similar += num_list1[i]
                num_list1[i]=num_list2[j]=0
                i+=1
                j+=1
            elif num_list1[i] < num_list2[j]:
                if c1==c2:similar += num_list1[i]
                num_list2[j]-=num_list1[i]
                num_list1[i]=0
                i+=1
            else:
                if c1==c2:similar += num_list2[j]
                num_list1[i]-=num_list2[j]
                num_list2[j]=0
                j+=1
        
        del num_list1, num_list2, char_list1, char_list2
        return f"{similar}/{total}"