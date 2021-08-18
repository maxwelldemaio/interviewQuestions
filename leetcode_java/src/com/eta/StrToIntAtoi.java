package com.eta;

public class StrToIntAtoi {
	public int myAtoi(String s) {
		if (s.equals("")) {
			return 0;
		}
		
		// Initialize sum, sign, and iter variables
		int res = 0, sign = 1, i = 0;
		
		// Go through whitespace
		while (i < s.length() && s.charAt(i) == ' ') {
			i++;
		}
		
		// Check for sign (and increment to keep going)
		if (i < s.length() && (s.charAt(i) == '-' || s.charAt(i) == '+')) {
			if (s.charAt(i++) == '-') {
				sign = -1;
			}
		}
		
        // Iterate through all digits of input
		// Only iterate while there is valid input
		// Make sure the res does not overflow the Integer max/min value
		while(i < s.length() && s.charAt(i) >= '0' && s.charAt(i) <= '9') {
			// handle int overflow
			if (res > Integer.MAX_VALUE / 10 || (res == Integer.MAX_VALUE / 10 && s.charAt(i) - '0' > 7)) {
				if (sign == -1) {
					return Integer.MIN_VALUE;
				}
				if (sign == 1) {
					return Integer.MAX_VALUE;
				}
			}
            res = res * 10 + Character.getNumericValue(s.charAt(i));
            i++;
		}
		
        return sign * res;
	}
}
