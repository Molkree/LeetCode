# https://leetcode.com/problems/container-with-most-water/
# 11. Container With Most Water


class Solution:
    def maxArea(self, heights: list[int]) -> int:  # noqa: N802
        area = 0
        left, right = 0, len(heights) - 1
        while left < right:
            area = max(area, (right - left) * min(heights[left], heights[right]))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return area


solution = Solution()


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
assert solution.maxArea(height) == 49

height = [1, 1]
assert solution.maxArea(height) == 1

height = [4, 3, 2, 1, 4]
assert solution.maxArea(height) == 16

height = [1, 2, 1]
assert solution.maxArea(height) == 2
