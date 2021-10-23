# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# 153. Find Minimum in Rotated Sorted Array


class Solution:
    def findMin(self, nums: list[int]) -> int:  # noqa: N802
        first_elem = nums[0]
        ind = len(nums) // 2
        if ind == 1:
            return min(nums)
        ceil = len(nums)
        while True:
            if ind + 1 == len(nums):
                return nums[0]
            if nums[ind] >= first_elem and nums[ind + 1] < first_elem:
                return nums[ind + 1]
            if nums[ind] > first_elem:
                ind = (ceil + ind) // 2
            else:
                ceil = ind
                ind //= 2


solution = Solution()


nums = [1, 2, 3, 4, 5]
assert solution.findMin(nums) == 1

nums = [3, 4, 5, 1, 2]
assert solution.findMin(nums) == 1

nums = [4, 5, 6, 7, 0, 1, 2]
assert solution.findMin(nums) == 0

nums = [11, 13, 15, 17]
assert solution.findMin(nums) == 11

nums = [11]
assert solution.findMin(nums) == 11

nums = [11, 12]
assert solution.findMin(nums) == 11

nums = [4, 1, 2, 3]
assert solution.findMin(nums) == 1

nums = [3, 1, 2]
assert solution.findMin(nums) == 1

nums = [1, 2, 3]
assert solution.findMin(nums) == 1

nums = [2, 1, 3]
assert solution.findMin(nums) == 1

nums = [12, 11]
assert solution.findMin(nums) == 11

nums = [4, 5, 6, 1, 2, 3]
assert solution.findMin(nums) == 1

nums = [5, 6, 1, 2, 3, 4]
assert solution.findMin(nums) == 1

nums = [6, 1, 2, 3, 4, 5]
assert solution.findMin(nums) == 1

nums = [3, 4, 5, 6, 1, 2]
assert solution.findMin(nums) == 1

nums = [2, 3, 4, 5, 6, 1]
assert solution.findMin(nums) == 1
