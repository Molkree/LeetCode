# https://leetcode.com/problems/4sum/
# 18. 4Sum


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:  # noqa: N802
        def two_sum(nums: list[int], target: int) -> list[list[int]]:
            result = list[list[int]]()
            low, high = 0, len(nums) - 1
            while low < high:
                cur_sum = nums[low] + nums[high]
                if cur_sum < target or low and nums[low - 1] == nums[low]:
                    low += 1
                elif (
                    cur_sum > target
                    or high < len(nums) - 1
                    and nums[high] == nums[high + 1]
                ):
                    high -= 1
                else:
                    result.append([nums[low], nums[high]])
                    low, high = low + 1, high - 1
            return result

        def k_sum(nums: list[int], target: int, k: int) -> list[list[int]]:
            average = target // k
            if not nums or average < nums[0] or nums[-1] < average:
                return []
            if k == 2:
                return two_sum(nums, target)
            result = list[list[int]]()
            for i in range(len(nums)):
                if i and nums[i - 1] == nums[i]:
                    continue
                for good_nums in k_sum(nums[i + 1 :], target - nums[i], k - 1):
                    result.append([nums[i]] + good_nums)
            return result

        nums.sort()
        return k_sum(nums, target, 4)


solution = Solution()


nums = [1, 0, -1, 0, -2, 2]
target = 0
assert sorted(solution.fourSum(nums, target)) == sorted(
    [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
)

nums = [2, 2, 2, 2, 2]
target = 8
assert sorted(solution.fourSum(nums, target)) == sorted([[2, 2, 2, 2]])

nums = [2, 2, 2, 3]
target = 8
assert sorted(solution.fourSum(nums, target)) == []

nums = [1, -2, -5, -4, -3, 3, 3, 5]
target = -11
assert sorted(solution.fourSum(nums, target)) == sorted([[-5, -4, -3, 1]])
