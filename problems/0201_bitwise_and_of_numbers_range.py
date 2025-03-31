# https://leetcode.com/problems/bitwise-and-of-numbers-range/
# 201. Bitwise AND of Numbers Range


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:  # noqa: N802
        # not cool solution
        # if left == 0 or left * 2 < right:
        #     return 0
        # result = left
        # if left % 2 != 0 and right > left:
        #     result &= result + 1
        #     left += 1
        # right = min(right, pow(2, math.ceil(math.log2(left) + 1)))
        # for i in range(left + 2, right + 1, 2):
        #     result &= i
        # return result
        # cool solution
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift


solution = Solution()

left = 5
right = 7
assert 4 == solution.rangeBitwiseAnd(left, right)

left = 0
right = 0
assert 0 == solution.rangeBitwiseAnd(left, right)

left = 1
right = 2147483647
assert 0 == solution.rangeBitwiseAnd(left, right)

left = 8
right = 16
assert 0 == solution.rangeBitwiseAnd(left, right)

left = 20000
right = 2147483647
assert 0 == solution.rangeBitwiseAnd(left, right)

left = 5
right = 8
assert 0 == solution.rangeBitwiseAnd(left, right)

left = 10
right = 12
assert 8 == solution.rangeBitwiseAnd(left, right)

left = 600000000
right = 2147483645
assert 0 == solution.rangeBitwiseAnd(left, right)
