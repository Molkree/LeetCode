# https://leetcode.com/problems/permutation-in-string/
# 567. Permutation in String


from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:  # noqa: N802
        if len(s1) > len(s2):
            return False
        s1_count = Counter(s1)
        sub_count = Counter(s2[: len(s1)])
        if s1_count == sub_count:
            return True
        for i in range(len(s2) - len(s1)):
            sub_count[s2[i]] -= 1
            sub_count[s2[i + len(s1)]] += 1
            if s1_count == sub_count:
                return True
        return False


solition = Solution()


s1 = "ab"
s2 = "eidbaooo"
assert solition.checkInclusion(s1, s2)

s1 = "ab"
s2 = "eidboaoo"
assert not solition.checkInclusion(s1, s2)

s1 = "dinitrophenylhydrazine"
s2 = "acetylphenylhydrazine"
assert not solition.checkInclusion(s1, s2)
