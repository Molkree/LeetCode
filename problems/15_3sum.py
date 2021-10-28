# https://leetcode.com/problems/3sum/
# 15. 3Sum


class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[list[int]]:
        num_set: set[int] = set()
        result: list[list[int]] = []
        for num in nums:
            if (other := target - num) in num_set:
                result.append([other, num])
            num_set.add(num)
        return result

    def threeSum(self, nums: list[int]) -> list[list[int]]:  # noqa: N802
        result: list[list[int]] = []
        triplets: set[tuple[int, ...]] = set()
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            for pair in self.two_sum(nums[i + 1 :], -nums[i]):
                if (triplet := tuple((nums[i], *pair))) not in triplets:
                    result.append([nums[i], *pair])
                    triplets.add(triplet)
        return result


solution = Solution()


nums = [-1, 0, 1, 2, -1, -4]
print(solution.threeSum(nums))
# [[-1,-1,2],[-1,0,1]]

nums: list[int] = []
assert [] == solution.threeSum(nums)

nums = [0]
assert [] == solution.threeSum(nums)

nums = [-1, 0, 1, 0]
print(solution.threeSum(nums))
# [[-1,0,1]]
