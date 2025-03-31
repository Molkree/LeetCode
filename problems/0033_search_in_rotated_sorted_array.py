# https://leetcode.com/problems/search-in-rotated-sorted-array/
# 33. Search in Rotated Sorted Array


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        if low < len(nums) and nums[low] == target:
            return low
        return -1


solution = Solution()


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
assert solution.search(nums, target) == 4

nums = [4, 5, 6, 7, 0, 1, 2]
target = 3
assert solution.search(nums, target) == -1

nums = [1]
target = 0
assert solution.search(nums, target) == -1

nums = [1, 3, 5]
target = 2
assert solution.search(nums, target) == -1
