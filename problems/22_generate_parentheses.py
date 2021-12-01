# https://leetcode.com/problems/generate-parentheses/
# 22. Generate Parentheses


from functools import cache
from itertools import product


class Solution:
    @cache
    def generateParenthesis(self, n: int) -> list[str]:  # noqa: N802
        if n == 1:
            return ["()"]
        parenthesis: set[str] = set()
        prev_parens = self.generateParenthesis(n - 1)
        for parens in prev_parens:
            parenthesis.add(f"({parens})")
        for count in range(1, n):
            prev_parens_a = self.generateParenthesis(count)
            prev_parens_b = self.generateParenthesis(n - count)
            for (parens_a, parens_b) in product(prev_parens_a, prev_parens_b):
                parenthesis.add(f"{parens_a}{parens_b}")
        return list(parenthesis)


solution = Solution()


n = 1
assert sorted(solution.generateParenthesis(n)) == sorted(["()"])

n = 2
assert sorted(solution.generateParenthesis(n)) == sorted(["()()", "(())"])

n = 3
assert sorted(solution.generateParenthesis(n)) == sorted(
    [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()",
    ]
)

n = 4
assert sorted(solution.generateParenthesis(n)) == sorted(
    [
        "(((())))",
        "((()()))",
        "((())())",
        "((()))()",
        "(()(()))",
        "(()()())",
        "(()())()",
        "(())(())",
        "(())()()",
        "()((()))",
        "()(()())",
        "()(())()",
        "()()(())",
        "()()()()",
    ]
)
