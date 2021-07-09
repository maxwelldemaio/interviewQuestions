package com.eta;

import java.util.List;

public class ThreeSum {
	public static int findStartingIndex(int[] nums, int target) {
		int index = -1;

		int start = 0;
		int end = nums.length - 1;

		// Binary search
		while (start <= end) {
			int mid = start + (end - start) / 2;
			// Greater than or equal to, so we get the first occurence
			if (nums[mid] >= target) {
				end = mid - 1;
			} else {
				start = mid + 1;
			}
			
			// Found
			if (nums[mid] == target) index = mid;
		}
		return index;
	}

	public static int findEndingIndex(int[] nums, int target) {
		int index = -1;

		int start = 0;
		int end = nums.length - 1;

		// Binary search
		while (start <= end) {
			int mid = start + (end - start) / 2;
			// Greater than or equal to, so we get the first occurence
			if (nums[mid] <= target) {
				start = mid + 1;
			} else {
				end = mid - 1;
			}
			
			// Found
			if (nums[mid] == target) index = mid;
		}
		return index;
	}

	public static int[] searchRange(int[] nums, int target) {
		int[] result = new int[2];
		// Find first and second elements
		result[0] = findStartingIndex(nums, target);
		result[1] = findEndingIndex(nums, target);
		return result;
	}

}
