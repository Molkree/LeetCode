# https://leetcode.com/problems/gas-station/
# 134. Gas Station


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:  # noqa: N802
        start_ind = 0
        while start_ind < len(gas):
            tank = gas[start_ind]
            can_complete = True
            for i in range(len(gas)):
                tank -= cost[(start_ind + i) % len(gas)]
                if tank < 0:
                    can_complete = False
                    start_ind = start_ind + i + 1
                    break
                tank += gas[(start_ind + i + 1) % len(gas)]
            if can_complete:
                return start_ind
        return -1


solution = Solution()


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
assert solution.canCompleteCircuit(gas, cost) == 3

gas = [2, 3, 4]
cost = [3, 4, 3]
assert solution.canCompleteCircuit(gas, cost) == -1
