package com.eta;

/* 1047 - https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
 * You are given a string s consisting of lowercase English letters. 
 * A duplicate removal consists of choosing two adjacent and equal letters and removing them.
 * We repeatedly make duplicate removals on s until we no longer can.
 * Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.
 */

public class RemoveAdjDupInStr {
	public String removeDuplicates(String s) {
		char[] stack = new char[s.length()];
		int i = 0;
		
		for (int j=0; j < s.length(); j++) {
			char currChar = s.charAt(j);
			
			// Check for adjacent duplicates by peeking top of stack
			// Also ignore if stack is empty
			if (i > 0 && stack[i-1] == currChar) {
				i--;
			} else {
				stack[i] = currChar;
				i++;
			}
		}
		
		return new String(stack, 0, i);
	}
}
