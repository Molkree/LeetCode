# https://leetcode.com/problems/jump-game-vi/
# 1696. Jump Game VI


from collections import deque


class Solution:
    def maxResult(self, nums: list[int], k: int) -> int:  # noqa: N802
        queue = deque([0])
        for index in range(1, len(nums)):
            nums[index] += nums[queue[0]]
            while queue and nums[queue[-1]] <= nums[index]:
                queue.pop()
            queue.append(index)
            if index - queue[0] == k:
                queue.popleft()
        return nums[-1]


solution = Solution()


nums = [1, -1, -2, 4, -7, 3]
k = 2
assert solution.maxResult(nums, k) == 7

nums = [10, -5, -2, 4, 0, 3]
k = 3
assert solution.maxResult(nums, k) == 17

nums = [1, -5, -20, 4, -1, 3, -6, -3]
k = 2
assert solution.maxResult(nums, k) == 0

nums = [100, -1, -100, -1, 100]
k = 2
assert solution.maxResult(nums, k) == 198
