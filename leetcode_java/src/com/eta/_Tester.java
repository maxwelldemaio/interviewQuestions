package com.eta;

public class _Tester {

	public static void main(String[] args) {
		// Note: for each problem we create static methods since you can
		// Access them without creating a new instance of the object
		
		// Test cases
		// create one linked list (true)
		ListNode node1 = new ListNode(2);
		node1.next = new ListNode(4);
		node1.next.next = new ListNode(2);
		
		// create another linked list (false)
		ListNode node2 = new ListNode(5);
		node2.next = new ListNode(6);
		node2.next.next = new ListNode(4);
		PalindromeLinkedList p = new PalindromeLinkedList();
		System.out.println(p.isPalindrome(node1));
	}
}
