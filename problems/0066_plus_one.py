# https://leetcode.com/problems/plus-one/
# 66. Plus One


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:  # noqa: N802
        # def plus(edit_index: int) -> None:
        #     nonlocal digits
        #     digits[edit_index] = (digits[edit_index] + 1) % 10
        #     if digits[edit_index] == 0:
        #         if edit_index == 0:
        #             digits = [1] + digits
        #         else:
        #             plus(edit_index - 1)

        # plus(len(digits) - 1)
        # return digits
        digits[-1] = (digits[-1] + 1) % 10
        if digits[-1] == 0:
            if len(digits) == 1:
                digits = [1] + digits
            else:
                digits = self.plusOne(digits[:-1]) + [digits[-1]]
        return digits


solution = Solution()


digits = [1, 2, 3]
assert solution.plusOne(digits) == [1, 2, 4]

digits = [4, 3, 2, 1]
assert solution.plusOne(digits) == [4, 3, 2, 2]

digits = [9]
assert solution.plusOne(digits) == [1, 0]

digits = [9, 9]
assert solution.plusOne(digits) == [1, 0, 0]
