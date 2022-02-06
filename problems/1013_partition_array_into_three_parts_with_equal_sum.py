# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/
# 1013. Partition Array Into Three Parts With Equal Sum


class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:  # noqa: N802
        all_sum = sum(arr)
        if all_sum % 3:
            return False
        target_sum = all_sum // 3
        left_sum = 0
        for i in range(len(arr) - 2):
            left_sum += arr[i]
            if left_sum == target_sum:
                mid_sum = 0
                for j in range(i + 1, len(arr) - 1):
                    mid_sum += arr[j]
                    if mid_sum == target_sum:
                        return sum(arr[j + 1 :]) == target_sum
        return False


solution = Solution()


arr = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]
assert solution.canThreePartsEqualSum(arr)

arr = [0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]
assert not solution.canThreePartsEqualSum(arr)

arr = [3, 3, 6, 5, -2, 2, 5, 1, -9, 4]
assert solution.canThreePartsEqualSum(arr)
