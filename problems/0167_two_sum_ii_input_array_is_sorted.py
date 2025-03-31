# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# 167. Two Sum II - Input Array Is Sorted


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:  # noqa: N802
        low, high = 0, len(numbers) - 1
        while low < high:
            cur_sum = numbers[low] + numbers[high]
            if cur_sum < target or low and numbers[low - 1] == numbers[low]:
                low += 1
            elif (
                cur_sum > target
                or high < len(numbers) - 1
                and numbers[high] == numbers[high + 1]
            ):
                high -= 1
            else:
                return [low + 1, high + 1]
        return []


solution = Solution()


numbers = [2, 7, 11, 15]
target = 9
assert solution.twoSum(numbers, target) == [1, 2]

numbers = [2, 3, 4]
target = 6
assert solution.twoSum(numbers, target) == [1, 3]

numbers = [-1, 0]
target = -1
assert solution.twoSum(numbers, target) == [1, 2]
