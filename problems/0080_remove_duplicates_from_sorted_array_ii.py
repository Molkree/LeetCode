# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# 80. Remove Duplicates from Sorted Array II


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:  # noqa: N802
        cur_num = nums[0]
        is_double = False
        k = 1
        for i in range(1, len(nums)):
            num = nums[i]
            if num == cur_num:
                if not is_double:
                    is_double = True
                    nums[k] = num
                    k += 1
            else:
                cur_num = num
                is_double = False
                nums[k] = num
                k += 1
        return k


solution = Solution()


nums = [1, 1, 1, 2, 2, 3]
k = 5
assert solution.removeDuplicates(nums) == k and nums[:k] == [1, 1, 2, 2, 3]

nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
k = 7
assert solution.removeDuplicates(nums) == k and nums[:k] == [0, 0, 1, 1, 2, 3, 3]
