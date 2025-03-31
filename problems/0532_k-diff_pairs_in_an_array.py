# https://leetcode.com/problems/k-diff-pairs-in-an-array/
# 532. K-diff Pairs in an Array


from collections import Counter


class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:  # noqa: N802
        # linear
        counter = Counter(nums)
        return sum(
            k > 0 and num + k in counter or k == 0 and counter[num] > 1
            for num in counter
        )
        # n * logn
        nums.sort()
        good_nums = set[int]()
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                diff = nums[j] - nums[i]
                if diff == k:
                    if nums[i] not in good_nums:
                        good_nums.add(nums[i])
                        count += 1
                        break
                elif diff > k:
                    break
        return count


solution = Solution()


nums = [3, 1, 4, 1, 5]
k = 2
assert solution.findPairs(nums, k) == 2

nums = [1, 2, 3, 4, 5]
k = 1
assert solution.findPairs(nums, k) == 4

nums = [1, 3, 1, 5, 4]
k = 0
assert solution.findPairs(nums, k) == 1
