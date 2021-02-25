# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head
        # Increment fast until we hit N
        # After we hit N, increment until fast.next = None
        # Also once N is hit, start incrementing slow
        # Then perform deletion
        for i in range(n):
            fast = fast.next

        # N == Length of list (delete first element)
        if fast is None:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head