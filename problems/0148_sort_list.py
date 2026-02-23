# https://leetcode.com/problems/sort-list/
# 148. Sort List


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:  # noqa: N802
        if not head or not head.next:
            return head

        def get_middle(head: ListNode) -> ListNode:
            prev: ListNode | None = None
            while head and head.next:
                prev = prev.next if prev else head
                head = head.next.next  # type: ignore
            middle = prev.next  # type: ignore
            prev.next = None  # type: ignore
            return middle  # type: ignore

        middle = get_middle(head)
        left = self.sortList(head)
        right = self.sortList(middle)

        def merge(left: ListNode, right: ListNode) -> ListNode:
            fake_head = ListNode(10**5 + 1)
            tail = fake_head
            while left and right:
                if left.val < right.val:
                    tail.next = left
                    left = left.next  # type: ignore
                    tail = tail.next
                else:
                    tail.next = right
                    right = right.next  # type: ignore
                    tail = tail.next
            tail.next = left or right
            return fake_head.next  # type: ignore

        return merge(left, right)
