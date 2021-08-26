package com.eta;

public class _Tester {

	public static void main(String[] args) {
		// Note: for each problem we create static methods since you can
		// Access them without creating a new instance of the object
		
		// Test cases
		
		// LL1
		ListNode head1 = new ListNode(3);
		ListNode node_1a = new ListNode(2);
		ListNode node_1b = new ListNode(0);
		ListNode node_1c = new ListNode(4);
		
		head1.next = node_1a;
		node_1a.next = node_1b;
		node_1b.next = node_1c;
		node_1c.next = node_1a; // cycle starts here
		
		// LL2
//		ListNode head2 = new ListNode();
		
		LinkedListCycle lc = new LinkedListCycle();
		System.out.println("Return value: " + lc.hasCycle(head1));
	}
}
