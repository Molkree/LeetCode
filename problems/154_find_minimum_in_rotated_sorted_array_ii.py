# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
# 154. Find Minimum in Rotated Sorted Array II


class Solution:
    def findMin(self, nums: list[int]) -> int:  # noqa: N802
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            elif nums[mid] < nums[high]:
                high = mid
            else:
                high -= 1
        return nums[low]


solution = Solution()


nums = [1, 3, 5]
assert solution.findMin(nums) == 1

nums = [2, 2, 2, 0, 1]
assert solution.findMin(nums) == 0

nums = [0, 0, 0, 0]
assert solution.findMin(nums) == 0

nums = [1, 3, 1, 1]
assert solution.findMin(nums) == 1

nums = [3, 1, 1, 1]
assert solution.findMin(nums) == 1

nums = [3, 1, 3, 3]
assert solution.findMin(nums) == 1

nums = [1, 1, 1, 1, 0]
assert solution.findMin(nums) == 0
