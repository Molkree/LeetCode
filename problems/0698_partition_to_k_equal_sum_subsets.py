# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
# 698. Partition to K Equal Sum Subsets


class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:  # noqa: N802
        total_sum = sum(nums)
        subset_target = total_sum // k
        if subset_target * k != total_sum:
            return False

        visited = [False] * len(nums)
        nums.sort(reverse=True)

        def can_partition(k: int, current_sum: int = 0, ind: int = 0) -> bool:
            if k == 1:
                return True
            if current_sum == subset_target:
                return can_partition(k - 1)
            for i in range(ind, len(nums)):
                if not visited[i] and current_sum + nums[i] <= subset_target:
                    visited[i] = True
                    if can_partition(k, current_sum + nums[i], i + 1):
                        return True
                    visited[i] = False
            return False

        return can_partition(k)


solution = Solution()

nums = [4, 3, 2, 3, 5, 2, 1]
k = 4
assert solution.canPartitionKSubsets(nums, k)

nums = [1, 2, 3, 4]
k = 3
assert not solution.canPartitionKSubsets(nums, k)

nums = [15, 3557, 42, 3496, 5, 81, 34, 95, 9, 81, 42, 106, 71]
k = 11
assert not solution.canPartitionKSubsets(nums, k)
