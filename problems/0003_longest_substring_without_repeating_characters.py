# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 3. Longest Substring Without Repeating Characters


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:  # noqa: N802
        # slow solution with len(dict)
        # sub_set: dict[str, int] = {}
        # max_len = 0
        # for ind, char in enumerate(s):
        #     if char not in sub_set:
        #         sub_set[char] = ind
        #     else:
        #         max_len = max(max_len, len(sub_set))
        #         old_ind = sub_set[char]
        #         sub_set = {
        #             char: ind
        #             for ind, char in enumerate(s[old_ind + 1 : ind + 1], old_ind + 1)
        #         }
        # return max(max_len, len(sub_set))
        # faster solution with two pointers
        sub_set = dict[str, int]()
        max_len = 0
        low, high = 0, 0
        while high < len(s):
            if (char := s[high]) in sub_set:
                max_len = max(max_len, high - low)
                low = max(low, sub_set[char] + 1)
            sub_set[char] = high
            high += 1
        return max(max_len, high - low)


solution = Solution()


s = "abcabcbb"
assert solution.lengthOfLongestSubstring(s) == 3

s = "bbbbb"
assert solution.lengthOfLongestSubstring(s) == 1

s = "pwwkew"
assert solution.lengthOfLongestSubstring(s) == 3

s = ""
assert solution.lengthOfLongestSubstring(s) == 0

s = "abcad"
assert solution.lengthOfLongestSubstring(s) == 4

s = "jbpnbwwd"
assert solution.lengthOfLongestSubstring(s) == 4

s = "abba"
assert solution.lengthOfLongestSubstring(s) == 2
