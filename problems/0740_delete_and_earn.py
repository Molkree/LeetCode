# https://leetcode.com/problems/delete-and-earn/
# 740. Delete and Earn


from collections import defaultdict
from functools import cache


class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:  # noqa: N802
        points = defaultdict[int, int](int)
        max_num = 0
        for num in nums:
            points[num] += num
            max_num = max(max_num, num)

        @cache
        def max_points(num: int) -> int:
            if num == 0:
                return 0
            if num == 1:
                return points[1]
            return max(points[num] + max_points(num - 2), max_points(num - 1))

        return max_points(max_num)


solution = Solution()


nums = [3, 4, 2]
assert solution.deleteAndEarn(nums) == 6

nums = [2, 2, 3, 3, 3, 4]
assert solution.deleteAndEarn(nums) == 9
