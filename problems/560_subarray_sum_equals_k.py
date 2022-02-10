# https://leetcode.com/problems/subarray-sum-equals-k/
# 560. Subarray Sum Equals K


from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:  # noqa: N802
        sums = defaultdict[int, int](int)
        sums[0] = 1
        prefix_sum = 0
        count = 0
        for num in nums:
            prefix_sum += num
            count += sums[prefix_sum - k]
            sums[prefix_sum] += 1
        return count


solution = Solution()


nums = [1, 1, 1]
k = 2
assert solution.subarraySum(nums, k) == 2

nums = [1, 2, 3]
k = 3
assert solution.subarraySum(nums, k) == 2
