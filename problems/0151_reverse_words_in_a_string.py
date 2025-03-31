# https://leetcode.com/problems/reverse-words-in-a-string/
# 151. Reverse Words in a String


class Solution:
    def reverseWords(self, s: str) -> str:  # noqa: N802
        return " ".join(reversed(s.split()))


solution = Solution()


s = "the sky is blue"
assert solution.reverseWords(s) == "blue is sky the"

s = "  hello world  "
assert solution.reverseWords(s) == "world hello"

s = "a good   example"
assert solution.reverseWords(s) == "example good a"

s = "  Bob    Loves  Alice   "
assert solution.reverseWords(s) == "Alice Loves Bob"

s = "Alice does not even like bob"
assert solution.reverseWords(s) == "bob like even not does Alice"
