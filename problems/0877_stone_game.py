# https://leetcode.com/problems/stone-game/
# 877. Stone Game


class Solution:
    def stoneGame(self, piles: list[int]) -> bool:  # noqa: N802
        # @cache
        # def score(left_pile: int, right_pile: int) -> int:
        #     if left_pile > right_pile:
        #         return 0
        #     player = (right_pile - left_pile) % 2
        #     if player:
        #         return max(
        #             piles[left_pile] + score(left_pile + 1, right_pile),
        #             piles[right_pile] + score(left_pile, right_pile - 1),
        #         )
        #     else:
        #         return min(
        #             score(left_pile + 1, right_pile) - piles[left_pile],
        #             score(left_pile, right_pile - 1) - piles[right_pile],
        #         )

        # return score(0, len(piles) - 1) > 0
        # first player always wins
        return True
