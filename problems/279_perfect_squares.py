# https://leetcode.com/problems/perfect-squares/
# 279. Perfect Squares


class Solution:
    def numSquares(self, n: int) -> int:  # noqa: N802
        square_sums: list[int] = [0]
        while len(square_sums) <= n:
            num = len(square_sums)
            num_squares = 10 ** 4
            for i in range(1, num + 1):
                if i * i > num:
                    break
                num_squares = min(num_squares, square_sums[num - i * i] + 1)
            square_sums.append(num_squares)
        return square_sums[n]


solution = Solution()


n = 1
assert 1 == solution.numSquares(n)

n = 12
assert 3 == solution.numSquares(n)

n = 13
assert 2 == solution.numSquares(n)
