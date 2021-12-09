# https://leetcode.com/problems/jump-game-iii/
# 1306. Jump Game III


class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:  # noqa: N802
        stack = [start]
        while stack:
            i = stack.pop()
            if arr[i] == 0:
                return True
            if (j := i - arr[i]) >= 0 and arr[j] >= 0:
                stack.append(j)
            if (j := i + arr[i]) < len(arr) and arr[j] >= 0:
                stack.append(j)
            arr[i] *= -1
        return False


solution = Solution()


arr = [4, 2, 3, 0, 3, 1, 2]
start = 5
assert solution.canReach(arr, start)

arr = [4, 2, 3, 0, 3, 1, 2]
start = 0
assert solution.canReach(arr, start)

arr = [3, 0, 2, 1, 2]
start = 2
assert not solution.canReach(arr, start)
