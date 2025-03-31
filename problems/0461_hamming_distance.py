# https://leetcode.com/problems/hamming-distance/
# 461. Hamming Distance


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:  # noqa: N802
        # first solution
        # x, y = sorted((x, y))
        # bin_x = bin(x)[2:]
        # bin_y = bin(y)[2:]
        # bin_x = "0" * (len(bin_y) - len(bin_x)) + bin_x
        # distance = 0
        # for i in range(len(bin_x)):
        #     if bin_x[-1 - i] != bin_y[-1 - i]:
        #         distance += 1
        # return distance
        # second shorter solution
        return bin(x ^ y).count("1")


solution = Solution()


print(bin(1))
print(bin(3))
x = 1
y = 4
assert solution.hammingDistance(x, y) == 2

x = 3
y = 1
assert solution.hammingDistance(x, y) == 1
