# https://leetcode.com/problems/linked-list-cycle-ii/
# 142. Linked List Cycle II


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next: ListNode | None = None


class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:  # noqa: N802
        slow = head
        fast = head
        while slow and fast:
            slow = slow.next
            fast = fast.next
            fast = fast and fast.next
            if slow and fast and slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next  # type: ignore
                    fast = fast.next  # type: ignore
                return slow


solution = Solution()


head = ListNode(1)
assert solution.detectCycle(head) is None

head = ListNode(1)
node = ListNode(2)
node.next = head
head.next = node
assert solution.detectCycle(head) == head
