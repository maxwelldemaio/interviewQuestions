package com.eta;

/* 209 - https://leetcode.com/problems/minimum-size-subarray-sum/
 * Given an array of positive integers nums and a positive integer target, 
 * return the minimal length of a contiguous subarray 
 * [numsl, numsl+1, ..., numsr-1, numsr] 
 * of which the sum is greater than or equal to target. 
 * If there is no such subarray, return 0 instead.
 */

public class MinSizeSubarraySum {
	public int minSubArrayLen(int target, int[] nums) {
		// Initialize 2 pointers to start
		int result = Integer.MAX_VALUE;
		int left = 0;
		int cumul_sum = 0;
		
		for (int i=0; i < nums.length; i++) {
			cumul_sum += nums[i];
			
			// Keep searching for smaller sub-arrays to form >= target
			while (cumul_sum >= target) {
				result = Math.min(result, (i + 1 - left));
				
				cumul_sum -= nums[left];
				left++;
			}
		}
		
		// If the value was never updated, auto return 0
        return (result != Integer.MAX_VALUE) ? result: 0;
    }
}
