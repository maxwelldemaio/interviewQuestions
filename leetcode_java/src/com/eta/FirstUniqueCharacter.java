package com.eta;

import java.util.HashMap;
import java.util.Map;

/* 387 - https://leetcode.com/problems/first-unique-character-in-a-string/
 * Given a string s, return the first non-repeating character 
 * in it and return its index. If it does not exist, return -1.
 */

public class FirstUniqueCharacter {
	public int firstUniqChar(String s) {
		Map<Character, Integer> freq = new HashMap<>();
		
		// Loop over string to generate frequency map
		for (int i = 0; i < s.length(); i++) {
			int prev = 0;
			 
            // get the previous count
            if (freq.get(s.charAt(i)) != null) {
                prev = freq.get(s.charAt(i));
            }
 
            freq.put(s.charAt(i), prev + 1);
		}
		
		// Find first non-repeating character
		for (int i = 0; i < s.length(); i++) {
            // If the count is 1, return the index
            if (freq.get(s.charAt(i)) == 1) {
                return i;
            }
		}
		
		// No repeating characters found
		return -1;
	}
}
