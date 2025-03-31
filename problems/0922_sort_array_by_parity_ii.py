# https://leetcode.com/problems/sort-array-by-parity-ii/
# 922. Sort Array By Parity II


class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:  # noqa: N802
        even_ind = 0
        odd_head = 1
        for even_ind in range(0, len(nums), 2):
            if nums[even_ind] % 2 != 0:
                for odd_ind in range(odd_head, len(nums), 2):
                    if nums[odd_ind] % 2 == 0:
                        odd_head = odd_ind
                        nums[odd_ind], nums[even_ind] = nums[even_ind], nums[odd_ind]
                        break
        return nums


def check_answer(nums: list[int]) -> bool:
    for ind, val in enumerate(nums):
        if ind % 2 != val % 2:
            return False
    return True


solution = Solution()

nums = [4, 2, 6, 5, 7, 1]
assert check_answer(solution.sortArrayByParityII(nums))

nums = [4, 2, 5, 7]
assert check_answer(solution.sortArrayByParityII(nums))

nums = [1, 0, 1, 0]
assert check_answer(solution.sortArrayByParityII(nums))

nums = [2, 3]
assert check_answer(solution.sortArrayByParityII(nums))

nums = [1, 4, 1, 3, 1, 4, 2, 2]
assert check_answer(solution.sortArrayByParityII(nums))
