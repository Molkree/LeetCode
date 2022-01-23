# https://leetcode.com/problems/sequential-digits/
# 1291. Sequential Digits


class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:  # noqa: N802
        digits = "123456789"
        min_length = len(str(low))
        nums = list[int]()
        ind = 0
        cur_len = min_length
        num = int(digits[ind : cur_len + ind])
        while num <= high and cur_len < 10:
            if num >= low:
                nums.append(num)
            ind += 1
            if ind + cur_len > len(digits):
                ind = 0
                cur_len += 1
            num = int(digits[ind : cur_len + ind])
        return nums


solution = Solution()


low = 100
high = 300
assert solution.sequentialDigits(low, high) == [123, 234]

low = 1000
high = 13000
assert solution.sequentialDigits(low, high) == [
    1234,
    2345,
    3456,
    4567,
    5678,
    6789,
    12345,
]

low = 200
high = 300
assert solution.sequentialDigits(low, high) == [234]

low = 10
high = 100
assert solution.sequentialDigits(low, high) == [12, 23, 34, 45, 56, 67, 78, 89]

low = 10
high = 57
assert solution.sequentialDigits(low, high) == [12, 23, 34, 45, 56]

assert len(solution.sequentialDigits(10, 1000000000)) == 36
