# https://leetcode.com/explore/item/3989
# 929. Unique Email Addresses


class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:  # noqa: N802
        unique_emails: set[str] = set()
        for email in emails:
            local_name, domain_name = email.split("@")
            local_name = local_name.split("+")[0].replace(".", "")
            unique_emails.add(f"{local_name}@{domain_name}")
        return len(unique_emails)


solution = Solution()

emails = [
    "test.email+alex@leetcode.com",
    "test.e.mail+bob.cathy@leetcode.com",
    "testemail+david@lee.tcode.com",
]
assert solution.numUniqueEmails(emails) == 2

emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
assert solution.numUniqueEmails(emails) == 3

emails = ["test.email+alex@leetcode.com", "test.email.leet+alex@code.com"]
assert solution.numUniqueEmails(emails) == 2
