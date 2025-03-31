# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# 17. Letter Combinations of a Phone Number


from collections import Counter
from itertools import product


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:  # noqa: N802
        if not digits:
            return []
        digit2letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        letters = [digit2letters[digit] for digit in digits]
        return list(map(lambda x: "".join(x), product(*letters)))


solution = Solution()


digits = "23"
assert Counter(solution.letterCombinations(digits)) == Counter(
    ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
)

digits = ""
assert Counter(solution.letterCombinations(digits)) == Counter([])

digits = "2"
assert Counter(solution.letterCombinations(digits)) == Counter(["a", "b", "c"])
