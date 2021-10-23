# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# 153. Find Minimum in Rotated Sorted Array


class Solution:
    def findMin(self, nums: list[int]) -> int:  # noqa: N802
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]


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
