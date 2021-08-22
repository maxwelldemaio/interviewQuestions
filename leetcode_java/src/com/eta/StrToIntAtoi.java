package com.eta;

/*
 * // Test cases
		String test0 = "";
		String test1 = "42"; //42
		String test2 = "  -42"; //-42
		String test3 = "4193 with words"; //4193
		String test4 = "words and 987"; //0
		String test5 = "-91283472332"; //-2147483648
		String test6 = " "; // 0
		
		StrToIntAtoi s = new StrToIntAtoi();
		System.out.println("Return value: " + s.myAtoi(test6));
 */

public class StrToIntAtoi {
	public int myAtoi(String s) {
		if (s.equals("")) {
			return 0;
		}
		
		// Initialize sum, sign, and iter variables
		int res = 0, sign = 1, i = 0;
		
		// Go through whitespace
		while (i < s.length() - 1 && s.charAt(i) == ' ') {
			i++;
		}
		
		// Check for sign (and increment to keep going)
		if (i < s.length() - 1 && (s.charAt(i) == '-' || s.charAt(i) == '+')) {
			if (s.charAt(i++) == '-') {
				sign = -1;
			}
		}
		
        // Iterate through all digits of input
		// Only iterate while there is valid input
		// Make sure the res does not overflow the Integer max/min value
		while(i < s.length() - 1 && s.charAt(i) >= '0' && s.charAt(i) <= '9') {
			// handle int overflow
			if (res > Integer.MAX_VALUE / 10 || (res == Integer.MAX_VALUE / 10 && s.charAt(i) - '0' > 7)) {
				if (sign == -1) {
					return Integer.MIN_VALUE;
				}
				if (sign == 1) {
					return Integer.MAX_VALUE;
				}
			}
            res = res * 10 + (s.charAt(i) - '0');
            i++;
		}
		
        return sign * res;
	}
}
