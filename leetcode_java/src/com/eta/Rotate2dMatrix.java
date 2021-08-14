package com.eta;

// Test cases
//	int[][] matrix = {{1,2,3},{4,5,6},{7,8,9}};
//	Rotate2dMatrix.rotate(matrix);

public class Rotate2dMatrix {
	public void rotate(int[][] matrix) {
		Integer temp2 = 0;
		
        for (int i = matrix.length - 1; i >= 0; i--) {
        	Integer temp = 0;
        	System.out.println("Row: " + i);
        	for (int j = 0; j < matrix[i].length; j++) {
        		matrix[temp][temp2] = matrix[i][j];
        		System.out.println(matrix[i][j]);
        		temp++;
        	}
        	temp2++;
        }
    }
}
