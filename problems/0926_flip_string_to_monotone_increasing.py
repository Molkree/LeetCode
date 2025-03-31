# https://leetcode.com/problems/flip-string-to-monotone-increasing
# 926. Flip String to Monotone Increasing


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:  # noqa: N802
        # smart counters solution
        ones = 0
        flips = 0
        for bit in s:
            if bit == "1":
                ones += 1
            else:
                flips += 1
            flips = min(flips, ones)
        return flips
        # prefix sums solution
        prefix_sums = [0]
        for bit in s:
            prefix_sums.append(prefix_sums[-1] + int(bit))
        return min(
            prefix_sums[i] + len(s) - i - prefix_sums[-1] + prefix_sums[i]
            for i in range(len(prefix_sums))
        )


solution = Solution()


s = "00110"
assert solution.minFlipsMonoIncr(s) == 1

s = "010110"
assert solution.minFlipsMonoIncr(s) == 2

s = "00011000"
assert solution.minFlipsMonoIncr(s) == 2
