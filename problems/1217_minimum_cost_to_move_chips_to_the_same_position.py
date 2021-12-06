# https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
# 1217. Minimum Cost to Move Chips to The Same Position


class Solution:
    def minCostToMoveChips(self, position: list[int]) -> int:  # noqa: N802
        even = 0
        for ind in position:
            if ind % 2 == 0:
                even += 1
        return min(even, len(position) - even)


solution = Solution()


position = [1, 2, 3]
assert solution.minCostToMoveChips(position) == 1

position = [2, 2, 2, 3, 3]
assert solution.minCostToMoveChips(position) == 2

position = [1, 1000000000]
assert solution.minCostToMoveChips(position) == 1
