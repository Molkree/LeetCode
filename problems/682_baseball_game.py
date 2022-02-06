# https://leetcode.com/problems/baseball-game/
# 682. Baseball Game


class Solution:
    def calPoints(self, ops: list[str]) -> int:  # noqa: N802
        stack = list[int]()
        for op in ops:
            match op:
                case "+":
                    stack.append(stack[-2] + stack[-1])
                case "D":
                    stack.append(stack[-1] * 2)
                case "C":
                    stack.pop()
                case _:
                    stack.append(int(op))
        return sum(stack)


solution = Solution()


ops = ["5", "2", "C", "D", "+"]
assert solution.calPoints(ops) == 30

ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
assert solution.calPoints(ops) == 27

ops = ["1"]
assert solution.calPoints(ops) == 1
