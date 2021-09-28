# https://leetcode.com/problems/min-stack/
# 155. Min Stack


class MinStack:
    _stack: list[tuple[int, int]]

    def __init__(self):
        self._stack: list[tuple[int, int]] = []
        self._min = None

    def push(self, val: int) -> None:
        if not self._stack:
            self._stack.append((val, val))
        else:
            self._stack.append((val, min(val, self._stack[-1][1])))

    def pop(self) -> None:
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1][0]

    def getMin(self) -> int:  # noqa: N802
        assert self._stack
        return self._stack[-1][1]


min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
assert -3 == min_stack.getMin()
min_stack.pop()
assert 0 == min_stack.top()
assert -2 == min_stack.getMin()
