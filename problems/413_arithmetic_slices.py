# https://leetcode.com/problems/arithmetic-slices/
# 413. Arithmetic Slices


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:  # noqa: N802
        if len(nums) < 3:
            return 0
        count = 0
        length = 2

        def count_arrays(length: int) -> int:
            n = length - 2
            a_1 = 1
            return int(n / 2 * (2 * a_1 + (n - 1)))

        for i in range(1, len(nums) - 1):
            if nums[i] - nums[i + 1] == nums[i - 1] - nums[i]:
                length += 1
            else:
                count += count_arrays(length)
                length = 2
        if length > 2:
            count += count_arrays(length)
        return count


solution = Solution()


nums = [1, 2, 3, 4]
assert solution.numberOfArithmeticSlices(nums) == 3

nums = [1]
assert solution.numberOfArithmeticSlices(nums) == 0

nums = [1, 2, 3, 0, -1, -2]
assert solution.numberOfArithmeticSlices(nums) == 2
