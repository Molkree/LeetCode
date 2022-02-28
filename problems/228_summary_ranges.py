# https://leetcode.com/problems/summary-ranges/
# 228. Summary Ranges


class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:  # noqa: N802
        if not nums:
            return []
        ranges = list[str]()
        start = nums[0]
        cur_num = nums[0]
        for num in nums[1:]:
            if num - cur_num > 1:
                if cur_num - start > 0:
                    ranges.append(f"{start}->{cur_num}")
                else:
                    ranges.append(f"{start}")
                start = num
            cur_num = num
        if cur_num - start > 0:
            ranges.append(f"{start}->{cur_num}")
        else:
            ranges.append(f"{start}")
        return ranges


solution = Solution()


nums = [0, 1, 2, 4, 5, 7]
assert solution.summaryRanges(nums) == ["0->2", "4->5", "7"]

nums = [0, 2, 3, 4, 6, 8, 9]
assert solution.summaryRanges(nums) == ["0", "2->4", "6", "8->9"]
