# https://leetcode.com/problems/find-all-anagrams-in-a-string/
# 438. Find All Anagrams in a String


from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:  # noqa: N802
        if len(p) > len(s):
            return []
        p_counter = Counter(p)
        counter = Counter(s[: len(p)])
        result = list[int]()
        if p_counter == counter:
            result.append(0)
        for i in range(len(s) - len(p)):
            counter[s[i]] -= 1
            counter[s[i + len(p)]] += 1
            if counter == p_counter:
                result.append(i + 1)
        return result


solution = Solution()


s = "cbaebabacd"
p = "abc"
assert solution.findAnagrams(s, p) == [0, 6]

s = "abab"
p = "ab"
assert solution.findAnagrams(s, p) == [0, 1, 2]

s = "a"
p = "ab"
assert solution.findAnagrams(s, p) == []
