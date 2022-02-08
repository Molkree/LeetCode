# https://leetcode.com/problems/add-digits/
# 258. Add Digits


class Solution:
    def addDigits(self, num: int) -> int:  # noqa: N802
        while num > 9:
            num = sum(map(int, str(num)))
        return num
        # smart solution
        if not num:
            return num
        digital_sum = num % 9
        return digital_sum if digital_sum else 9


solution = Solution()


num = 38
assert solution.addDigits(num) == 2

num = 0
assert solution.addDigits(num) == 0

num = 54
assert solution.addDigits(num) == 9

num = 9
assert solution.addDigits(num) == 9
