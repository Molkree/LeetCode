# https://leetcode.com/problems/search-insert-position/
# 35. Search Insert Position


import bisect


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:  # noqa: N802
        # lazy solution
        return bisect.bisect_left(nums, target)
        # custom binary search
        # low, high = 0, len(nums)
        # while low < high:
        #     middle = (low + high) // 2
        #     guess = nums[middle]
        #     if guess == target:
        #         return middle
        #     elif guess < target:
        #         low = middle + 1
        #     else:
        #         high = middle
        # return low


solution = Solution()


nums = [1, 3, 5, 6]
target = 5
assert solution.searchInsert(nums, target) == 2

nums = [1, 3, 5, 6]
target = 2
assert solution.searchInsert(nums, target) == 1

nums = [1, 3, 5, 6]
target = 7
assert solution.searchInsert(nums, target) == 4

nums = [1, 3, 5, 6]
target = 0
assert solution.searchInsert(nums, target) == 0

nums = [1]
target = 0
assert solution.searchInsert(nums, target) == 0

nums = [1, 3]
target = 2
assert solution.searchInsert(nums, target) == 1
