# https://leetcode.com/problems/kth-largest-element-in-an-array/
# 215. Kth Largest Element in an Array


import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:  # noqa: N802
        # O(nlogn) where n is the length of nums
        # return sorted(nums)[-k]
        # O(nlogk) where n is the length of nums
        heap = list[int]()
        for num in nums[:k]:
            heapq.heappush(heap, num)
        for num in nums[k:]:
            if heap[0] < num:
                heapq.heappushpop(heap, num)
        return heap[0]


solution = Solution()


nums = [3, 2, 1, 5, 6, 4]
k = 2
assert solution.findKthLargest(nums, k) == 5

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
assert solution.findKthLargest(nums, k) == 4

nums = [5, 2, 4, 1, 3, 6, 0]
k = 4
assert solution.findKthLargest(nums, k) == 3
