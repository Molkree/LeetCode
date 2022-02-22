# https://leetcode.com/problems/excel-sheet-column-number/
# 171. Excel Sheet Column Number


import string


class Solution:
    def titleToNumber(self, column_title: str) -> int:  # noqa: N802
        table = dict(zip(string.ascii_uppercase, range(1, 27)))
        ind = 0
        result = 0
        for char in column_title[::-1]:
            result += table[char] * 26**ind
            ind += 1
        return result


solution = Solution()


column_title = "A"
assert solution.titleToNumber(column_title) == 1

column_title = "AA"
assert solution.titleToNumber(column_title) == 27

column_title = "AB"
assert solution.titleToNumber(column_title) == 28

column_title = "BA"
assert solution.titleToNumber(column_title) == 53

column_title = "ZY"
assert solution.titleToNumber(column_title) == 701
