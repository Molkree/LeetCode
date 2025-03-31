# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# 26. Remove Duplicates from Sorted Array


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:  # noqa: N802
        if not nums:
            return 0
        cur_num = nums[0]
        k = 1
        for i in range(1, len(nums)):
            num = nums[i]
            if num != cur_num:
                cur_num = num
                nums[k] = num
                k += 1
        return k


solution = Solution()


nums = [1, 1, 2]
k = 2
assert solution.removeDuplicates(nums) == k and nums[:k] == [1, 2]

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = 5
assert solution.removeDuplicates(nums) == k and nums[:k] == [0, 1, 2, 3, 4]
