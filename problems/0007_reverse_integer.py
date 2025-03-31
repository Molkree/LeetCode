# https://leetcode.com/problems/reverse-integer/
# 7. Reverse Integer


class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        x = int("".join(reversed(str(abs(x)))))
        if len(bin(x)) > 33:
            return 0
        return -x if negative else x


solution = Solution()


x = 123
assert solution.reverse(x) == 321

x = -123
assert solution.reverse(x) == -321

x = 120
assert solution.reverse(x) == 21

x = 1534236469
assert solution.reverse(x) == 0
