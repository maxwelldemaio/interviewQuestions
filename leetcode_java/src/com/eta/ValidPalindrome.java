package com.eta;

public class ValidPalindrome {
	public boolean isPalindrome(String s) {
		// Initialize pointers
		int left = 0;
		int right = s.length() - 1;
		
		while (left < right) {
			// Check if valid alpha-numeric character
			while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
				left++;
			}
			while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
				right--;
			}
			
			// Compare
			if(left < right && Character.toLowerCase(s.charAt(left++)) != Character.toLowerCase(s.charAt(right--))) {
				return false;
			}
		}
		
		return true;
	}
}
