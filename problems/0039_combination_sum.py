# https://leetcode.com/problems/combination-sum/
# 39. Combination Sum


class Solution:
    def combinationSum(  # noqa: N802
        self, candidates: list[int], target: int
    ) -> list[list[int]]:
        result = list[list[int]]()

        def find_sum(index: int, nums: list[int]) -> None:
            cur_sum = sum(nums)
            if cur_sum > target:
                return
            if cur_sum == target:
                result.append(nums)
                return
            for i in range(index, len(candidates)):
                find_sum(i, nums + [candidates[i]])

        find_sum(0, [])
        return result


solution = Solution()


candidates = [2, 3, 5]
target = 8
print(solution.combinationSum(candidates, target))
