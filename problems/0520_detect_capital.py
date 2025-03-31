# https://leetcode.com/problems/detect-capital/
# 520. Detect Capital


class Solution:
    def detectCapitalUse(self, word: str) -> bool:  # noqa: N802
        cases = [char.isupper() for char in word]
        return all(cases) or not any(cases) or cases[0] and not any(cases[1:])


solution = Solution()


word = "USA"
assert solution.detectCapitalUse(word)

word = "leetcode"
assert solution.detectCapitalUse(word)

word = "Google"
assert solution.detectCapitalUse(word)

word = "FlaG"
assert not solution.detectCapitalUse(word)
