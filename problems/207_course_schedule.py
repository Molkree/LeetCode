# https://leetcode.com/problems/course-schedule/
# 207. Course Schedule


from collections import defaultdict


class Solution:
    def canFinish(  # noqa: N802
        self, num_courses: int, prerequisites: list[list[int]]
    ) -> bool:
        neighbours: defaultdict[int, set[int]] = defaultdict(set[int])
        for start, end in prerequisites:
            neighbours[start].add(end)
        todo = [False] * num_courses
        done = [False] * num_courses

        def acyclic(course: int) -> bool:
            if todo[course]:
                return False
            if done[course]:
                return True
            todo[course] = True
            done[course] = True
            for prereq in neighbours[course]:
                if not acyclic(prereq):
                    return False
            todo[course] = False
            return True

        for course in range(num_courses):
            if not done[course] and not acyclic(course):
                return False
        return True


solution = Solution()


num_courses = 2
prerequisites = [[1, 0]]
assert solution.canFinish(num_courses, prerequisites)

num_courses = 2
prerequisites = [[0, 1]]
assert solution.canFinish(num_courses, prerequisites)

num_courses = 2
prerequisites = [[1, 0], [0, 1]]
assert not solution.canFinish(num_courses, prerequisites)

num_courses = 5
prerequisites = [[1, 4], [2, 4], [3, 1], [3, 2]]
assert solution.canFinish(num_courses, prerequisites)

num_courses = 7
prerequisites = [[1, 0], [0, 3], [0, 2], [3, 2], [2, 5], [4, 5], [5, 6], [2, 4]]
assert solution.canFinish(num_courses, prerequisites)
