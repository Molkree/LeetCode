# https://leetcode.com/problems/remove-element/
# 27. Remove Element


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:  # noqa: N802
        k = 0
        for i in range(len(nums)):
            num = nums[i]
            if num != val:
                nums[k] = num
                k += 1
        return k


solution = Solution()


nums = [3, 2, 2, 3]
val = 3
k = 2
assert solution.removeElement(nums, val) == k and sorted(nums[:k]) == sorted([2, 2])

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
k = 5
assert solution.removeElement(nums, val) == k and sorted(nums[:k]) == sorted(
    [0, 1, 4, 0, 3]
)
