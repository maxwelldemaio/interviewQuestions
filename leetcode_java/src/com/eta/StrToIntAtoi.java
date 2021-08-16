package com.eta;

public class StrToIntAtoi {
	public int myAtoi(String s) {
		// Have boolean for negative
		Boolean isNegative = false;
		int sum = 0;
		
		// Start reading characters of str
		for (int i = 0; i < s.length(); i++) {
			char c = s.charAt(i);
			
			// Read in and ignore any leading whitespace
			if (Character.isWhitespace(c)) {
				continue;
			}
			System.out.println(c);
		}
		
		return sum;
	}
}
