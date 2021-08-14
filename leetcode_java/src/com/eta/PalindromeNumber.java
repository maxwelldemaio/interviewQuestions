package com.eta;

public class PalindromeNumber {
	public boolean isPalindrome(int x) {
		if (x == 0) {
			return true;
		}
		
		// Divisible by 10 or negative number
		if (x < 0 || x % 10 == 0) {
			return false;
		}
        
		int reversedInt = 0;
		while (x > reversedInt) {
			// Get last digit of x
			int pop = x % 10;
			x /= 10;
			
			reversedInt = (reversedInt * 10) + pop;
		}
		
		if (x == reversedInt || x == reversedInt / 10) {
			return true;
		} else {
			return false;
		}
    }
}
