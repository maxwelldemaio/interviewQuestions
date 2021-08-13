package com.eta;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;

public class _Tester {

	public static void main(String[] args) {
		// Note: for each problem we create static methods since you can
		// Access them without creating a new instance of the object
		
		// Test cases
		// create one linked list (true)
		ListNode1 node1 = new ListNode1(2);
		node1.next = new ListNode1(4);
		node1.next.next = new ListNode1(2);
		
		// create another linked list (false)
		ListNode1 node2 = new ListNode1(5);
		node2.next = new ListNode1(6);
		node2.next.next = new ListNode1(4);
		
		System.out.println(PalindromeLinkedList.isPalindrome(node1));
	}
}
