package com.eta;

public class _Tester {

	public static void main(String[] args) {
		// Note: for each problem we create static methods since you can
		// Access them without creating a new instance of the object
		
		// Test cases
		int[] arr = {3,2,4};
		int[] answer = TwoSum.getTwoSum(arr, 6);
		for (int i = 0; i < answer.length; i++) {
			System.out.println(answer[i]);
		}
	}

}
