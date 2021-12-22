# https://leetcode.com/problems/valid-number/
# 65. Valid Number


class Solution:
    def isNumber(self, s: str) -> bool:  # noqa: N802
        def is_integer(s: str) -> bool:
            return (
                len(s) > 0
                and all(char.isdigit() for char in s)
                or len(s) > 1
                and s[0] in "+-"
                and all(char.isdigit() for char in s[1:])
            )

        def is_decimal(s: str) -> bool:
            if not s:
                return False
            if s[0] in "+-":
                s = s[1:]
            parts = s.split(".")
            if len(parts) != 2:
                return False
            int_part, frac_part = parts

            def nonempty_part(part: str) -> bool:
                return len(part) > 0 and all(char.isdigit() for char in part)

            return (
                nonempty_part(int_part)
                and len(frac_part) == 0
                or len(int_part) == 0
                and nonempty_part(frac_part)
                or nonempty_part(int_part)
                and nonempty_part(frac_part)
            )

        parts = s.lower().split("e")
        if len(parts) > 2:
            return False
        if not is_decimal(parts[0]) and not is_integer(parts[0]):
            return False
        if len(parts) == 2 and not is_integer(parts[1]):
            return False
        return True


solution = Solution()


s = "2"
assert solution.isNumber(s)

s = "0089"
assert solution.isNumber(s)

s = "-0.1"
assert solution.isNumber(s)

s = "+3.14"
assert solution.isNumber(s)

s = "4."
assert solution.isNumber(s)

s = "-.9"
assert solution.isNumber(s)

s = "2e10"
assert solution.isNumber(s)

s = "-90E3"
assert solution.isNumber(s)

s = "3e+7"
assert solution.isNumber(s)

s = "+6e-1"
assert solution.isNumber(s)

s = "53.5e93"
assert solution.isNumber(s)

s = "-123.456e789"
assert solution.isNumber(s)

s = "abc"
assert not solution.isNumber(s)

s = "1a"
assert not solution.isNumber(s)

s = "1e"
assert not solution.isNumber(s)

s = "e3"
assert not solution.isNumber(s)

s = "99e2.5"
assert not solution.isNumber(s)

s = "--6"
assert not solution.isNumber(s)

s = "-+3"
assert not solution.isNumber(s)

s = "95a54e53"
assert not solution.isNumber(s)

s = "0"
assert solution.isNumber(s)

s = "e"
assert not solution.isNumber(s)

s = "."
assert not solution.isNumber(s)

s = ".1"
assert solution.isNumber(s)
