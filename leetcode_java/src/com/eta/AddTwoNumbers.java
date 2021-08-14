package com.eta;


//ListNode node1 = new ListNode(2);
//node1.next = new ListNode(4);
//node1.next.next = new ListNode(3);
//
//ListNode node2 = new ListNode(5);
//node2.next = new ListNode(6);
//node2.next.next = new ListNode(4);
//
//addTwoNumbers(node1, node2);

public class AddTwoNumbers {
	
	public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
		// Start a new LL with default 0 value on first node
		// Point to head node of LL
		ListNode l3Head = new ListNode(0);
		ListNode l3 = l3Head;
		
		while (l1 != null || l2 != null) {
            System.out.println("ListNode1 value: " + l1.val);
            System.out.println("ListNode2 value: " + l2.val);
            l1 = l1.next;
            l2 = l2.next;
        }
		
		int carry = 0;
		while (l1 != null || l2 != null) {
			// Basically if one ll is longer, we can have default 0s for values
			// We can do this w/ ternary conditions or just if/elses
            int l1_val = (l1 != null) ? l1.val : 0;
            int l2_val = (l2 != null) ? l2.val : 0;
            
            int currSum = l1_val + l2_val + carry;
            // Calculate carry value (this will also update it for each)
            // Note: rounds down to zero if less than 10
            carry = currSum / 10;
            // Grab last digit
            int lastDigit = currSum % 10;
            
            // Update user-defined LL 
            ListNode newNode = new ListNode(lastDigit);
            l3.next = newNode;
            
            // Continue traversing (if not at end of LL)
            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
            l3 = l3.next;
        }
		
		// Check if the result will be greater like 900 + 900 = 1800 (0018)
		if (carry > 0) {
			ListNode newNode = new ListNode(carry);
			l3.next = newNode;
		}
		
        return l3Head.next;
	}
}
