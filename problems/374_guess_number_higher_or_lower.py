# https://leetcode.com/problems/guess-number-higher-or-lower/
# 374. Guess Number Higher or Lower


def guess(num: int) -> int:
    return 0


class Solution:
    def guessNumber(self, n: int) -> int:  # noqa: N802
        pick = n // 2
        lower = 1
        upper = n
        next_guess: int = guess(pick)
        while next_guess:
            if next_guess < 0:
                upper = pick - 1
            else:
                lower = pick + 1
            pick = (upper + lower) // 2
            next_guess = guess(pick)
        return pick
