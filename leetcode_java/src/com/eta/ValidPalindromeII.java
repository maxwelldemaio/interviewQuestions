package com.eta;

/* 680 - https://leetcode.com/problems/valid-palindrome-ii/
 * Given a string s, return true if the s 
 * can be a palindrome after deleting at most one character from it.
 */

public class ValidPalindromeII {
	public boolean isPalindrome(String s, int i, int j) {
		while (i < j) {
			if(s.charAt(i++) != s.charAt(j--)) {
				return false;
			}
		}
		return true;
	}
	
	public boolean isPalindromeII(String s) {
		// Initialize pointers
		int i = 0;
		int j = s.length() - 1;
		
		while (i < j) {
			// Don't match
			if (s.charAt(i) != s.charAt(j)) {
				return isPalindrome(s, i+1, j) || isPalindrome(s, i, j-1);
			}
			
			i++;
			j--;
		}
		
		return true;
	}
}
