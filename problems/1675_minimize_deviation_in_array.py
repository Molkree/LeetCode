# https://leetcode.com/problems/minimize-deviation-in-array/
# 1675. Minimize Deviation in Array


import heapq


class Solution:
    def minimumDeviation(self, nums: list[int]) -> int:  # noqa: N802
        potentials = list[tuple[int, int]]()
        for num in nums:
            is_even = num % 2 == 0
            max_potential = num if is_even else num * 2
            min_potential = num
            if is_even:
                while min_potential % 2 == 0:
                    min_potential //= 2
            potentials.append((min_potential, max_potential))
        heapq.heapify(potentials)
        max_value = max(val for val, _ in potentials)
        diff = max_value - potentials[0][0]
        while True:
            current_value, max_potential = potentials[0]
            if max_potential > current_value:
                heapq.heapreplace(potentials, (current_value * 2, max_potential))
            else:
                break
            max_value = max(max_value, current_value * 2)
            new_diff = max_value - potentials[0][0]
            if new_diff < diff:
                diff = new_diff
        return diff


solution = Solution()


nums = [1, 2, 3, 4]
assert solution.minimumDeviation(nums) == 1

nums = [4, 1, 5, 20, 3]
assert solution.minimumDeviation(nums) == 3

nums = [2, 10, 8]
assert solution.minimumDeviation(nums) == 3

nums = [778, 846, 733]
assert solution.minimumDeviation(nums) == 113
