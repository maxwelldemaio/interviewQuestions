package com.eta;

import java.util.HashSet;
import java.util.Set;

// Test
// {{'5','3','.','.','7','.','.','.','.'},{'6','.','.','1','9','5','.','.','.'},{'.','9','8','.','.','.','.','6','.'},{'8','.','.','.','6','.','.','.','3'},{'4','.','.','8','.','3','.','.','1'},{'7','.','.','.','2','.','.','.','6'},{'.','6','.','.','.','.','2','8','.'},{'.','.','.','4','1','9','.','.','5'},{'.','.','.','.','8','.','.','7','9'}}

public class ValidSudoku {
	public boolean isValidSudoku(char[][] board) {
		System.out.println("Board:");
		for (int i = 0; i < 9; i++) {
			System.out.println(board[i]);
		}
		
		// Set -> no duplicates
		// Array List -> can have duplicates
		// Hashset -> hashing algorithm(value) -> index based on value
		// Since its a set we won't have duplicate indexes
		Set<String> seen = new HashSet<>();
		System.out.println();
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				char currVal = board[i][j];
				
				// If not empty sudoku space
				if (currVal != '.') {
					if (!seen.add(currVal + " found in row " + i) || 
							!seen.add(currVal + " found in column " + j) || 
							!seen.add(currVal + " found in subbox " + i/3 + "-" + j/3)) {
						return false;
					}
				}
			}
		}
        return true;
    }
}
