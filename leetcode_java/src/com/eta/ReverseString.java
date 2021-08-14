package com.eta;

public class ReverseString {
	public void makeReverse(char[] s) {
		// Strings are immutable, char arrays are though!
		// Note: if passed string, char[] chars = s.toCharArray();
		
		// Initialize two pointers
		int left = 0;
		int right = s.length - 1;
		
		while (left < right) {
			// Create temp and swap
			char temp = s[left];
			s[left++] = s[right];
			s[right--] = temp;
		}
		System.out.println(s);
	}

}
