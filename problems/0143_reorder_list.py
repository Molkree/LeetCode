# https://leetcode.com/problems/reorder-list/
# 143. Reorder List


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode | None) -> None:  # noqa: N802
        if not head:
            return
        lst = list[ListNode]()
        head_copy = head
        while head_copy:
            lst.append(head_copy)
            head_copy = head_copy.next
        head_copy = head
        count = 1
        i = 0
        while True:
            head_copy.next = lst[-1 - i]
            head_copy = head_copy.next
            count += 1
            if count < len(lst):
                head_copy.next = lst[i + 1]
                head_copy = head_copy.next
                count += 1
            else:
                head_copy.next = None
                break
            i += 1


solution = Solution()


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
solution.reorderList(head)
