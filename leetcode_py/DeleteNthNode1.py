# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return head

        itr = head
        length = 1
        # Figure out length of LL
        while itr.next:
            length += 1
            itr = itr.next

        # Delete (length - n)th node
        itr = head
        count = 0
        while itr:
            if count == length - n - 1:
                itr.next = itr.next.next
                return head
            count += 1
            itr = itr.next

        # Size and n = 1
        if length == 1 and n == 1:
            head = None
        # Size of 2 and n = 1
        else:
            head = head.next

        return head
