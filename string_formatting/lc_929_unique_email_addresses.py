# https://leetcode.com/problems/unique-email-addresses/description/
"""
Solution : using set()
Runtime 41 ms Beats 99.8%
Memory 13.9 MB Beats 67.17%

TC: O(n*m) where n=len(emails), m = max(len(emails[i]))
SC: O(n*m)
"""
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniques=set()
        for email in emails:
            local_name, domain_name = email.split('@')
            local_name = local_name.split("+")[0].replace(".","")
            if local_name+"@"+domain_name not in uniques:
                uniques.add(local_name+"@"+domain_name)
        return len(uniques)