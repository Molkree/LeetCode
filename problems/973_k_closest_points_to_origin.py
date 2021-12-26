# https://leetcode.com/problems/k-closest-points-to-origin/
# 973. K Closest Points to Origin


class Solution:
    def kClosest(  # noqa: N802
        self, points: list[list[int]], k: int
    ) -> list[list[int]]:
        # this naive approach is faster than 98.86% of Python3 online submissions
        points.sort(key=lambda point: point[0] ** 2 + point[1] ** 2)
        return points[:k]


solution = Solution()


points = [[1, 3], [-2, 2]]
k = 1
assert sorted(solution.kClosest(points, k)) == sorted([[-2, 2]])

points = [[3, 3], [5, -1], [-2, 4]]
k = 2
assert sorted(solution.kClosest(points, k)) == sorted([[3, 3], [-2, 4]])
