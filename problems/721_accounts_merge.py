# https://leetcode.com/problems/accounts-merge/
# 721. Accounts Merge


from collections import defaultdict


class DSU:
    def __init__(self, n: int) -> None:
        self.parents = list(range(n))

    def find(self, x: int) -> int:
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, child: int, parent: int) -> None:
        self.parents[self.find(child)] = self.find(parent)


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:  # noqa: N802
        dsu = DSU(len(accounts))

        # Create unions between indexes
        email2index: dict[str, int] = {}
        for index, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in email2index:
                    dsu.union(index, email2index[email])
                email2index[email] = index

        # Append emails to correct index
        index2emails: defaultdict[int, list[str]] = defaultdict(list)
        for email, name in email2index.items():
            index2emails[dsu.find(name)].append(email)

        return [[accounts[i][0]] + sorted(emails) for i, emails in index2emails.items()]


solution = Solution()


accounts = [
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["Mary", "mary@mail.com"],
    ["John", "johnnybravo@mail.com"],
]
assert sorted(solution.accountsMerge(accounts)) == sorted(
    [
        ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
)

accounts = [
    ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
    ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
    ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
    ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
    ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"],
]
assert sorted(solution.accountsMerge(accounts)) == sorted(
    [
        ["Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"],
        ["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"],
        ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"],
        ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"],
        ["Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"],
    ]
)
