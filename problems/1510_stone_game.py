# https://leetcode.com/problems/stone-game-iv/
# 1510. Stone Game IV


from functools import cache


@cache
def winner_square_game(n: int) -> bool:
    if n == 0:
        return False
    num = int(n**0.5)
    while num >= 1:
        if not winner_square_game(n - num * num):
            return True
        num -= 1
    return False


class Solution:
    def winnerSquareGame(self, n: int) -> bool:  # noqa: N802
        return winner_square_game(n)


solution = Solution()


n = 1
assert solution.winnerSquareGame(n)

n = 2
assert not solution.winnerSquareGame(n)

n = 4
assert solution.winnerSquareGame(n)
