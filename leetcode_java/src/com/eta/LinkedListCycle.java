package com.eta;

import java.util.HashMap;
import java.util.Map;

public class LinkedListCycle {
	public boolean hasCycle(ListNode head) {
		// Create new hashmap to store hashCodes and indexes
		int i = 0;
		Map<Integer, Integer> code_map = new HashMap<>();
		
		// loop
		while(head != null) {
			System.out.println("Value: " + head.val);
			if (code_map.containsKey(head.hashCode())) {
				return true;
			}
			
			// add hashcode to map
			code_map.put(head.hashCode(), i);
			
			// continue
			head = head.next;
			i++;
		}
        return false;
    }
}
