# https://leetcode.com/problems/counting-bits/
# 338. Counting Bits


class Solution:
    def countBits(self, n: int) -> list[int]:  # noqa: N802
        # O(n * longn)
        return [i.bit_count() for i in range(n + 1)]
        # O(n) but it actually runs slower :)
        ans = [0, 1]
        i = 2
        count = 2
        while i < n + 1:
            real_count = min(count, n - i + 1)
            ans += [i + 1 for i in ans[:real_count]]
            i += real_count
            count *= 2
        return ans[: n + 1]


solution = Solution()


n = 2
assert solution.countBits(n) == [0, 1, 1]

n = 5
assert solution.countBits(n) == [0, 1, 1, 2, 1, 2]
