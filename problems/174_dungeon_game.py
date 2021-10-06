# https://leetcode.com/problems/dungeon-game/
# 174. Dungeon Game


class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:  # noqa: N802
        height = len(dungeon)
        width = len(dungeon[0])
        for i in range(height - 1, -1, -1):
            for j in range(width - 1, -1, -1):
                if i == height - 1 and j == width - 1:
                    dungeon[i][j] = 1 - min(dungeon[i][j], 0)
                elif j == width - 1:
                    dungeon[i][j] = max(dungeon[i + 1][j] - dungeon[i][j], 1)
                elif i == height - 1:
                    dungeon[i][j] = max(dungeon[i][j + 1] - dungeon[i][j], 1)
                else:
                    dungeon[i][j] = max(
                        min(dungeon[i + 1][j], dungeon[i][j + 1]) - dungeon[i][j], 1
                    )
        return dungeon[0][0]


solution = Solution()

dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
assert 7 == solution.calculateMinimumHP(dungeon)

dungeon = [[0]]
assert 1 == solution.calculateMinimumHP(dungeon)
