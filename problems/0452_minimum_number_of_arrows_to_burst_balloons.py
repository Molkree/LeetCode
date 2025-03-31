# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
# 452. Minimum Number of Arrows to Burst Balloons


class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:  # noqa: N802
        points.sort()
        arrows = 1
        min_end = 2**31
        for start, end in points:
            if start > min_end:
                arrows += 1
                min_end = end
            else:
                min_end = min(min_end, end)
        return arrows


solution = Solution()


points = [[10, 16], [2, 8], [1, 6], [7, 12]]
assert solution.findMinArrowShots(points) == 2

points = [[1, 2], [3, 4], [5, 6], [7, 8]]
assert solution.findMinArrowShots(points) == 4

points = [[1, 2], [2, 3], [3, 4], [4, 5]]
assert solution.findMinArrowShots(points) == 2
