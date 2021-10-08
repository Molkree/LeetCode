# https://leetcode.com/problems/jump-game/
# 55. Jump Game


class Solution:
    def can_jump_from_ind(self, ind: int, nums: list[int]) -> bool:
        if ind == len(nums) - 1:
            return True
        if nums[ind] == 0:
            return False
        for i in range(nums[ind]):
            if self.can_jump_from_ind(ind + i + 1, nums):
                return True
        return False

    def canJump(self, nums: list[int]) -> bool:  # noqa: N802
        return self.can_jump_from_ind(0, nums)


solution = Solution()

nums = [2, 3, 1, 1, 4]
assert solution.canJump(nums)

nums = [3, 2, 1, 0, 4]
assert not solution.canJump(nums)
