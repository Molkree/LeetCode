# https://leetcode.com/problems/largest-divisible-subset/
# 368. Largest Divisible Subset


class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:  # noqa: N802
        subsets: dict[int, list[int]] = {1: []}
        for num in sorted(nums):
            subsets[num] = (
                max(
                    (subsets[seen_num] for seen_num in subsets if num % seen_num == 0),
                    key=len,
                )
                + [num]
            )
        return max(subsets.values(), key=len)


solution = Solution()


nums = [1, 2, 4, 8]
print(solution.largestDivisibleSubset(nums))

nums = [2, 4, 6, 12, 18, 60, 600]
print(solution.largestDivisibleSubset(nums))
