# https://leetcode.com/problems/largest-rectangle-in-histogram/
# 84. Largest Rectangle in Histogram


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:  # noqa: N802
        leftmost_height = [-1] * len(heights)
        for i in range(1, len(heights)):
            leftmost = i - 1
            while leftmost > -1 and heights[leftmost] >= heights[i]:
                leftmost = leftmost_height[leftmost]
            leftmost_height[i] = leftmost
        rightmost_height = [len(heights)] * len(heights)
        for i in range(len(heights) - 2, -1, -1):
            rightmost = i + 1
            while rightmost < len(heights) and heights[rightmost] >= heights[i]:
                rightmost = rightmost_height[rightmost]
            rightmost_height[i] = rightmost
        return max(
            height * (rightmost_height[i] - leftmost_height[i] - 1)
            for i, height in enumerate(heights)
        )


solution = Solution()


heights = [2, 1, 5, 6, 2, 3]
assert solution.largestRectangleArea(heights) == 10

heights = [2, 4]
assert solution.largestRectangleArea(heights) == 4

heights = [0]
assert solution.largestRectangleArea(heights) == 0

heights = [2, 0, 2]
assert solution.largestRectangleArea(heights) == 2
