# https://leetcode.com/problems/reorder-data-in-log-files/
# 937. Reorder Data in Log Files


class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:  # noqa: N802
        def comparator(log: str) -> tuple[bool, str, str]:
            id, rest = log.split(" ", 1)
            return (False, rest, id) if rest[0].isalpha() else (True, "", "")

        return sorted(logs, key=comparator)


solution = Solution()


logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
assert solution.reorderLogFiles(logs) == [
    "let1 art can",
    "let3 art zero",
    "let2 own kit dig",
    "dig1 8 1 5 1",
    "dig2 3 6",
]

logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
assert solution.reorderLogFiles(logs) == [
    "g1 act car",
    "a8 act zoo",
    "ab1 off key dog",
    "a1 9 2 3 1",
    "zo4 4 7",
]
