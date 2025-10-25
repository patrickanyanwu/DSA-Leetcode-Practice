"""
    Use a set which holds each unique email address,
    now for each email we split it into 2 parts
    local name and domain name.
    for the local name we remove any dots from the name
    then we only look at everything before a + sign
    and then we recontruct the email and add it to the result set,
    then return the length of the result set.
    O(n ^ 2) time O(n) space.
"""

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()

        for email in emails:
            local_name, domain_name = email.split("@")
            local_name = local_name.replace(".", "")
            local_name = local_name.split("+")[0]
            result.add(local_name + "@" + domain_name)
        return len(result)