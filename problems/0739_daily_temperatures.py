# https://leetcode.com/problems/daily-temperatures/
# 739. Daily Temperatures


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:  # noqa: N802
        stack: list[int] = []
        result: list[int] = [0] * len(temperatures)
        for day, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                result[stack[-1]] = day - stack[-1]
                stack.pop()
            stack.append(day)
        return result


solution = Solution()


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
assert solution.dailyTemperatures(temperatures) == [1, 1, 4, 2, 1, 1, 0, 0]

temperatures = [30, 40, 50, 60]
assert solution.dailyTemperatures(temperatures) == [1, 1, 1, 0]

temperatures = [30, 60, 90]
assert solution.dailyTemperatures(temperatures) == [1, 1, 0]
