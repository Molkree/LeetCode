# https://leetcode.com/problems/valid-parentheses/
# 20. Valid Parentheses


class Solution:
    def isValid(self, s: str) -> bool:  # noqa: N802
        pairs = {"(": ")", "{": "}", "[": "]"}
        stack = list[str]()
        for parenthesis in s:
            if parenthesis in "({[":
                stack.append(parenthesis)
            elif not stack or pairs[stack.pop()] != parenthesis:
                return False
        return not stack


solution = Solution()

s = "()"
assert solution.isValid(s)

s = "()[]{}"
assert solution.isValid(s)

s = "(]"
assert not solution.isValid(s)

s = "([)]"
assert not solution.isValid(s)

s = "{[]}"
assert solution.isValid(s)

s = "("
assert not solution.isValid(s)

s = ")"
assert not solution.isValid(s)
