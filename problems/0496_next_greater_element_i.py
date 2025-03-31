# https://leetcode.com/problems/next-greater-element-i/
# 496. Next Greater Element I


class Solution:
    def nextGreaterElement(  # noqa: N802
        self, nums1: list[int], nums2: list[int]
    ) -> list[int]:
        # naive O(len(nums1) * len(nums2)) solution
        # result: list[int] = []
        # for num1 in nums1:
        #     next_greatest = -1
        #     for j, num2 in enumerate(nums2):
        #         if num1 == num2:
        #             for k in range(j + 1, len(nums2)):
        #                 if nums2[k] > num1:
        #                     next_greatest = nums2[k]
        #                     break
        #         if next_greatest != -1:
        #             break
        #     result.append(next_greatest)
        # return result
        #
        # elegant O(len(nums1) + len(nums2)) solution
        stack: list[int] = []
        greater_elements: dict[int, int] = {}
        for num2 in nums2:
            while stack and num2 > stack[-1]:
                greater_elements[stack.pop()] = num2
            stack.append(num2)
        return [greater_elements.setdefault(num1, -1) for num1 in nums1]


solution = Solution()


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
assert [-1, 3, -1] == solution.nextGreaterElement(nums1, nums2)

nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
assert [3, -1] == solution.nextGreaterElement(nums1, nums2)
