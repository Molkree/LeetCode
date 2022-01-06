# https://leetcode.com/problems/car-pooling/
# 1094. Car Pooling


from itertools import accumulate


class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:  # noqa: N802
        stops = [0] * 1001
        for num_passengers, start, end in trips:
            stops[start] += num_passengers
            stops[end] -= num_passengers
        return all(stop <= capacity for stop in accumulate(stops))


solution = Solution()


trips = [[2, 1, 5], [3, 3, 7]]
capacity = 4
assert not solution.carPooling(trips, capacity)

trips = [[2, 1, 5], [3, 3, 7]]
capacity = 5
assert solution.carPooling(trips, capacity)

trips = [[3, 3, 7], [2, 1, 5]]
capacity = 4
assert not solution.carPooling(trips, capacity)

trips = [[3, 3, 7], [2, 1, 5]]
capacity = 5
assert solution.carPooling(trips, capacity)

trips = [[1, 1, 10], [2, 1, 5]]
capacity = 2
assert not solution.carPooling(trips, capacity)

trips = [[1, 1, 10], [2, 2, 5]]
capacity = 2
assert not solution.carPooling(trips, capacity)

trips = [[1, 1, 10], [2, 2, 5]]
capacity = 3
assert solution.carPooling(trips, capacity)

trips = [[1, 1, 10], [2, 2, 15]]
capacity = 3
assert solution.carPooling(trips, capacity)

trips = [[9, 3, 6], [8, 1, 7], [8, 4, 9], [4, 2, 9]]
capacity = 28
assert not solution.carPooling(trips, capacity)

trips = [[2, 1, 5], [3, 5, 7]]
capacity = 3
assert solution.carPooling(trips, capacity)

trips = [[1, 3, 6], [8, 4, 6], [4, 4, 8]]
capacity = 12
assert not solution.carPooling(trips, capacity)
