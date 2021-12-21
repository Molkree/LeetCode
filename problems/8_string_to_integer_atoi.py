# https://leetcode.com/problems/string-to-integer-atoi/
# 8. String to Integer (atoi)


class Solution:
    def myAtoi(self, s: str) -> int:  # noqa: N802
        s = s.lstrip()
        if not s:
            return 0
        negative = s[0] == "-"
        if s[0] in "-+":
            s = s[1:]
        if not s:
            return 0
        num_s = ""
        for char in s:
            if char.isdigit():
                num_s += char
            else:
                break
        if not num_s:
            return 0
        num = int(num_s)
        num = -num if negative else num
        if num < -(2 ** 31):
            num = -(2 ** 31)
        elif 2 ** 31 - 1 < num:
            num = 2 ** 31 - 1
        return num


solution = Solution()


s = "42"
assert solution.myAtoi(s) == 42

s = "   -42"
assert solution.myAtoi(s) == -42

s = "4193 with words"
assert solution.myAtoi(s) == 4193

s = "0032"
assert solution.myAtoi(s) == 32

s = "-2147483649"
assert solution.myAtoi(s) == -2147483648

s = "2147483650"
assert solution.myAtoi(s) == 2147483647

s = ".1"
assert solution.myAtoi(s) == 0
