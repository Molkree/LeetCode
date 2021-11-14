# https://leetcode.com/problems/rearrange-spaces-between-words/
# 1592. Rearrange Spaces Between Words


class Solution:
    def reorderSpaces(self, text: str) -> str:  # noqa: N802
        words = text.split()
        total_spaces = len(text) - sum(len(word) for word in words)
        word_count = len(words)
        spaces_in_between = total_spaces // (word_count - 1) if word_count > 1 else 0
        spaces_in_tail = (
            total_spaces % (word_count - 1) if word_count > 1 else total_spaces
        )
        return (" " * spaces_in_between).join(words) + " " * spaces_in_tail


solution = Solution()


text = "  this   is  a sentence "
assert solution.reorderSpaces(text) == "this   is   a   sentence"

text = " practice   makes   perfect"
assert solution.reorderSpaces(text) == "practice   makes   perfect "

text = "hello   world"
assert solution.reorderSpaces(text) == "hello   world"

text = "  walks  udp package   into  bar a"
assert solution.reorderSpaces(text) == "walks  udp  package  into  bar  a "

text = "a"
assert solution.reorderSpaces(text) == "a"

text = "  a"
assert solution.reorderSpaces(text) == "a  "
