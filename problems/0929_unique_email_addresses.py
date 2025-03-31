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
assert 2 == solution.numUniqueEmails(emails)

emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
assert 3 == solution.numUniqueEmails(emails)

emails = ["test.email+alex@leetcode.com", "test.email.leet+alex@code.com"]
assert 2 == solution.numUniqueEmails(emails)
