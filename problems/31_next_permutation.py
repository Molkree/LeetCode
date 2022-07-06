# https://leetcode.com/problems/next-permutation/
# 31. Next Permutation


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:  # noqa: N802
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1 :] = reversed(nums[i + 1 :])


solution = Solution()


nums = [1, 2, 3]
solution.nextPermutation(nums)
assert nums == [1, 3, 2]

nums = [2, 3, 1]
solution.nextPermutation(nums)
assert nums == [3, 1, 2]

nums = [3, 2, 1]
solution.nextPermutation(nums)
assert nums == [1, 2, 3]

nums = [1, 1, 5]
solution.nextPermutation(nums)
assert nums == [1, 5, 1]

nums = [0, 1, 1]
solution.nextPermutation(nums)
assert nums == [1, 0, 1]

nums = [1, 2, 1, 3]
solution.nextPermutation(nums)
assert nums == [1, 2, 3, 1]

nums = [1, 2, 3, 1]
solution.nextPermutation(nums)
assert nums == [1, 3, 1, 2]

nums = [0, 1, 2, 1]
solution.nextPermutation(nums)
assert nums == [0, 2, 1, 1]

nums = [1, 3, 2]
solution.nextPermutation(nums)
assert nums == [2, 1, 3]
