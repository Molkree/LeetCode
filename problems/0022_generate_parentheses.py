# https://leetcode.com/problems/generate-parentheses/
# 22. Generate Parentheses


from functools import cache
from itertools import product


@cache
def generate_parenthesis(n: int) -> list[str]:
    if n == 1:
        return ["()"]
    parenthesis: set[str] = set()
    prev_parens = generate_parenthesis(n - 1)
    for parens in prev_parens:
        parenthesis.add(f"({parens})")
    for count in range(1, n):
        prev_parens_a = generate_parenthesis(count)
        prev_parens_b = generate_parenthesis(n - count)
        for parens_a, parens_b in product(prev_parens_a, prev_parens_b):
            parenthesis.add(f"{parens_a}{parens_b}")
    return list(parenthesis)


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:  # noqa: N802
        return generate_parenthesis(n)


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
