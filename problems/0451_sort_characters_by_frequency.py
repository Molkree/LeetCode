# https://leetcode.com/problems/sort-characters-by-frequency/
# 451. Sort Characters By Frequency


from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:  # noqa: N802
        return "".join(
            char * count
            for char, count in sorted(Counter(s).items(), key=lambda item: -item[1])
        )
