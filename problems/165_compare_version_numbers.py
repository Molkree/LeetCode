# https://leetcode.com/problems/compare-version-numbers/
# 165. Compare Version Numbers


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:  # noqa: N802
        revisions1 = list(map(int, version1.split(".")))
        revisions2 = list(map(int, version2.split(".")))
        revisions1_len = len(revisions1)
        revisions2_len = len(revisions2)
        for i in range(min(revisions1_len, revisions2_len)):
            if revisions1[i] < revisions2[i]:
                return -1
            if revisions1[i] > revisions2[i]:
                return 1
        if revisions1_len < revisions2_len:
            if any(revision > 0 for revision in revisions2[revisions1_len:]):
                return -1
        elif revisions1_len > revisions2_len:
            if any(revision > 0 for revision in revisions1[revisions2_len:]):
                return 1
        return 0


solution = Solution()


version1 = "1.01"
version2 = "1.001"
assert solution.compareVersion(version1, version2) == 0

version1 = "1.0"
version2 = "1.0.0"
assert solution.compareVersion(version1, version2) == 0

version1 = "0.1"
version2 = "1.1"
assert solution.compareVersion(version1, version2) == -1
