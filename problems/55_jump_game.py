# https://leetcode.com/problems/jump-game/
# 55. Jump Game


class Solution:
    def canJump(self, nums: list[int]) -> bool:  # noqa: N802
        max_index = 0
        for index, jump_length in enumerate(nums):
            if max_index < index:
                return False
            max_index = max(max_index, index + jump_length)
            if max_index >= len(nums) - 1:
                return True
        return False


solution = Solution()

nums = [2, 3, 1, 1, 4]
assert solution.canJump(nums)

nums = [3, 2, 1, 0, 4]
assert not solution.canJump(nums)

nums = [2, 0]
assert solution.canJump(nums)

nums = [1, 2, 3]
assert solution.canJump(nums)
