# https://leetcode.com/problems/palindrome-partitioning/
# 131. Palindrome Partitioning


from functools import cache


class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result: list[list[str]] = []

        @cache
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        def dfs(
            s: str, start: int, current_list: list[str], result: list[list[str]]
        ) -> None:
            if start == len(s):
                result += [list(current_list)]
            for end in range(start, len(s)):
                if is_palindrome(s[start : end + 1]):
                    current_list.append(s[start : end + 1])
                    dfs(s, end + 1, current_list, result)
                    current_list.pop()

        dfs(s, 0, [], result)
        return result


solution = Solution()

s = "a"
assert sorted(solution.partition(s)) == sorted([["a"]])

s = "aa"
assert sorted(solution.partition(s)) == sorted([["a", "a"], ["aa"]])

s = "aab"
assert sorted(solution.partition(s)) == sorted([["a", "a", "b"], ["aa", "b"]])

s = "efe"
assert sorted(solution.partition(s)) == sorted([["e", "f", "e"], ["efe"]])
