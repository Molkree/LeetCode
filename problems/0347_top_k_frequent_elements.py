# https://leetcode.com/problems/top-k-frequent-elements/
# 347. Top K Frequent Elements


from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:  # noqa: N802
        return [value for value, _ in Counter(nums).most_common(k)]


solution = Solution()


nums = [1, 1, 1, 2, 2, 3]
k = 2
assert sorted(solution.topKFrequent(nums, k)) == sorted([1, 2])

nums = [1]
k = 1
assert sorted(solution.topKFrequent(nums, k)) == sorted([1])
