# https://leetcode.com/problems/longest-consecutive-sequence/
# 128. Longest Consecutive Sequence


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:  # noqa: N802
        nums_set = set(nums)
        max_len = 0
        for num in nums:
            if num - 1 not in nums_set:
                curr_len = 1
                while num + 1 in nums_set:
                    curr_len += 1
                    num += 1
                max_len = max(max_len, curr_len)
        return max_len


solution = Solution()


nums = [100, 4, 200, 1, 3, 2]
assert solution.longestConsecutive(nums) == 4

nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
assert solution.longestConsecutive(nums) == 9
