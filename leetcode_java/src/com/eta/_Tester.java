package com.eta;

public class _Tester {

	public static void main(String[] args) {
		// Note: for each problem we create static methods since you can
		// Access them without creating a new instance of the object
		
		// Test cases
		String test0 = "";
		String test1 = "42"; //42
		String test2 = "  -42"; //-42
		String test3 = "4193 with words"; //4193
		String test4 = "words and 987"; //0
		String test5 = "-91283472332"; //-2147483648
		String test6 = " "; // 0
		
		StrToIntAtoi s = new StrToIntAtoi();
		System.out.println("Return value: " + s.myAtoi(test6));
	}
}
