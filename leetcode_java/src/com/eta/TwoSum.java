package com.eta;

import java.util.HashMap;
import java.util.Map;

/*
 * Given an array of integers nums and an integer target, 
 * return indices of the two numbers such that they add up to target.
 * You may assume that each input would have exactly one solution, 
 * and you may not use the same element twice.
 * You can return the answer in any order.
 */

public class TwoSum {
	public int[] getTwoSum(int[] nums, int target) {
		// Create new hashmap to store complements and indexes
		Map<Integer, Integer> num_map = new HashMap<>();
		
		// Loop until we find a match of number/complement
		for (int i = 0; i < nums.length; i++) {
			if (num_map.containsKey(nums[i])) {
				return new int[] {num_map.get(nums[i]), i};
			}
			
			// No match, store complement and index in HashMap
			num_map.put(target - nums[i], i);
		}
		
		// Error no match found
		return new int[] {};
	}
}
