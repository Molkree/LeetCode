# https://leetcode.com/problems/reverse-words-in-a-string-iii/
# 557. Reverse Words in a String III


class Solution:
    def reverseWords(self, s: str) -> str:  # noqa: N802
        return " ".join("".join(reversed(word)) for word in s.split())


solution = Solution()


s = "Let's take LeetCode contest"
assert solution.reverseWords(s) == "s'teL ekat edoCteeL tsetnoc"

s = "God Ding"
assert solution.reverseWords(s) == "doG gniD"
