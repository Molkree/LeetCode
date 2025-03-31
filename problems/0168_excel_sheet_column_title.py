# https://leetcode.com/problems/excel-sheet-column-title/
# 168. Excel Sheet Column Title


import string


class Solution:
    def convertToTitle(self, column_number: int) -> str:  # noqa: N802
        table = dict(zip(range(1, 26), string.ascii_uppercase))
        table[0] = "Z"
        result = ""
        while column_number > 0:
            column_number, letter = divmod(column_number, 26)
            result = table[letter] + result
            if (column_number, letter) == (1, 0):
                break
            if not letter:
                column_number -= 1
        return result


solution = Solution()


column_number = 1
assert solution.convertToTitle(column_number) == "A"

column_number = 28
assert solution.convertToTitle(column_number) == "AB"

column_number = 52
assert solution.convertToTitle(column_number) == "AZ"

column_number = 701
assert solution.convertToTitle(column_number) == "ZY"
