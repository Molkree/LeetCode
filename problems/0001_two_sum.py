# https://leetcode.com/problems/two-sum/
# 1. Two Sum


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:  # noqa: N802
        indexes = dict[int, int]()
        for index, num in enumerate(nums):
            if (other := target - num) in indexes:
                return [indexes[other], index]
            indexes[num] = index
        return []


solution = Solution()


nums = [2, 7, 11, 15]
target = 9
assert solution.twoSum(nums, target) == [0, 1]

nums = [3, 2, 4]
target = 6
assert solution.twoSum(nums, target) == [1, 2]

nums = [3, 3]
target = 6
assert solution.twoSum(nums, target) == [0, 1]
