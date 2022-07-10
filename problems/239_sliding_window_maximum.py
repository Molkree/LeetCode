# https://leetcode.com/problems/sliding-window-maximum/
# 239. Sliding Window Maximum


from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:  # noqa: N802
        queue = deque[int]()
        result = list[int]()
        counter = 0
        for index, num in enumerate(nums):
            while queue and nums[queue[-1]] < num:
                queue.pop()
            queue.append(index)
            if index - queue[0] == k:
                queue.popleft()
            counter += 1
            if counter >= k:
                result.append(nums[queue[0]])
        return result


solution = Solution()


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
assert solution.maxSlidingWindow(nums, k) == [3, 3, 5, 5, 6, 7]

nums = [1]
k = 1
assert solution.maxSlidingWindow(nums, k) == [1]

nums = [1, 3, 1, 2, 0, 5]
k = 3
assert solution.maxSlidingWindow(nums, k) == [3, 3, 2, 5]
