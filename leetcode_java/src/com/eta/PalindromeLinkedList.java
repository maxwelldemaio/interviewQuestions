package com.eta;


public class PalindromeLinkedList {
	public ListNode reversed(ListNode head) {
		// Reverse linked list from given node
		ListNode newHead = null;
		while (head != null) {
			ListNode temp = head.next;
			head.next = newHead;
			
			newHead = head;
			head = temp;
		}
		return newHead;
	}
	
	public boolean isPalindrome(ListNode head) {
		if (head == null) {
			return true;
		}
		
		// Two pointers to traverse
		ListNode slow = head;
		ListNode fast = head;
		
		// get slow  to the half way point
		// we do this by going 2 nodes at a time with fast
		while(fast.next != null && fast.next.next != null) {
			fast = fast.next.next;
			slow = slow.next;
		}
		
		
		ListNode secondHalfHead = reversed(slow.next);
		ListNode firstHalfHead = head;
		
		while(secondHalfHead != null && firstHalfHead != null) {
			// Compare the values (second half [reversed] and first half [normal])
			if (secondHalfHead.val != firstHalfHead.val) {
				return false;
			}
			secondHalfHead = secondHalfHead.next;
			firstHalfHead = firstHalfHead.next;
		}
		
		return true;
    }
}
