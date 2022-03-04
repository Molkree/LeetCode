# https://leetcode.com/problems/champagne-tower/
# 799. Champagne Tower


from math import isclose


class Solution:
    def champagneTower(  # noqa: N802
        self, poured: int, query_row: int, query_glass: int
    ) -> float:
        tower = [[0.0] * (i + 1) for i in range(101)]
        tower[0][0] = poured

        for row in range(query_row + 1):
            for column in range(row + 1):
                excess = (tower[row][column] - 1) / 2
                if excess > 0:
                    tower[row + 1][column] += excess
                    tower[row + 1][column + 1] += excess

        return min(1, tower[query_row][query_glass])


solution = Solution()


poured = 1
query_row = 1
query_glass = 1
assert isclose(solution.champagneTower(poured, query_row, query_glass), 0.00000)

poured = 2
query_row = 1
query_glass = 1
assert isclose(solution.champagneTower(poured, query_row, query_glass), 0.50000)

poured = 6
query_row = 2
query_glass = 0
assert isclose(solution.champagneTower(poured, query_row, query_glass), 0.75000)

poured = 6
query_row = 3
query_glass = 1
assert isclose(solution.champagneTower(poured, query_row, query_glass), 0.25000)

poured = 100000009
query_row = 33
query_glass = 17
assert isclose(solution.champagneTower(poured, query_row, query_glass), 1.00000)

poured = 1000000000
query_row = 99
query_glass = 99
assert isclose(solution.champagneTower(poured, query_row, query_glass), 0.00000)
