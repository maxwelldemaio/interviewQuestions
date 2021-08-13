package com.eta;

import java.util.ArrayList;
import java.util.List;

// test cases:

// Definition for singly-linked list.
class ListNode1 {
     int val;
     ListNode1 next;
     
     // constructors
     ListNode1() {}
     ListNode1(int val) { this.val = val; }
     ListNode1(int val, ListNode1 next) { this.val = val; this.next = next; }
 }

public class PalindromeLinkedList {
	public static ListNode1 reversed(ListNode1 head) {
		// Reverse linked list from given node
		ListNode1 newHead = null;
		while (head != null) {
			ListNode1 temp = head.next;
			head.next = newHead;
			
			newHead = head;
			head = temp;
		}
		return newHead;
	}
	
	public static boolean isPalindrome(ListNode1 head) {
		if (head == null) {
			return true;
		}
		
		// Two pointers to traverse
		ListNode1 slow = head;
		ListNode1 fast = head;
		
		// get slow  to the half way point
		// we do this by going 2 nodes at a time with fast
		while(fast.next != null && fast.next.next != null) {
			fast = fast.next.next;
			slow = slow.next;
		}
		
		
		ListNode1 secondHalfHead = reversed(slow.next);
		ListNode1 firstHalfHead = head;
		
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
