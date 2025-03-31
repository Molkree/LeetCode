# https://leetcode.com/problems/queue-reconstruction-by-height/
# 406. Queue Reconstruction by Height


class Solution:
    def reconstructQueue(  # noqa: N802
        self, people: list[list[int]]
    ) -> list[list[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        result = list[list[int]]()
        for person in people:
            result.insert(person[1], person)
        return result


solution = Solution()


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
assert solution.reconstructQueue(people) == [
    [5, 0],
    [7, 0],
    [5, 2],
    [6, 1],
    [4, 4],
    [7, 1],
]

people = [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]
assert solution.reconstructQueue(people) == [
    [4, 0],
    [5, 0],
    [2, 2],
    [3, 2],
    [1, 4],
    [6, 0],
]

people = [[2, 0], [2, 1]]
assert solution.reconstructQueue(people) == [[2, 0], [2, 1]]
