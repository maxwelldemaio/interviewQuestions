""" Create a game of Tic Tac Toe
0's represent emptiness, 1's represent Xs,
2's represent Os
"""
import os
os.system("cls") # clear for linux


class Board():
    def __init__(self):
        """ Initialize empty board """
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    
    def display(self):
        print(f"{self.cells[0]} | {self.cells[1]} | {self.cells[2]}")
        print("---------")
        print(f"{self.cells[3]} | {self.cells[4]} | {self.cells[5]}")
        print("---------")
        print(f"{self.cells[6]} | {self.cells[7]} | {self.cells[8]}")

    def update_cell(self, cell_num, player):
        """ Update cell in the board """
        # Make sure space if not already taken
        if self.cells[cell_num] == " ":
            self.cells[cell_num] = player

    def is_winner(self, player):
        for combo in [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]:
            win = True
            for cell in combo:
                # If any in combination don't work, it's not a win
                if self.cells[cell] != player:
                    win = False
            if win:
                return win
        return False

    def reset(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def is_tie(self):
        used_cells = 0
        for cell in self.cells:
            if cell != " ":
                used_cells += 1
        if used_cells == 9:
            return True
        else:
            return False


# Make board instance
board = Board()


def refresh_screen():
    # Clear the screen, printer header, show board
    os.system("cls")
    print("Tic-Tac-Toe:\n")
    board.display()


# Start game of Tic-Tac-Toe with our board instance
while True:
    refresh_screen()

    # Get X input
    x_choice = int(input("\nX) Please choose a space, 1-9: ")) - 1
    # Update board
    board.update_cell(x_choice, "X")
    refresh_screen()
    # Check for X win
    if board.is_winner("X"):
        print("\n X wins!\n")
        play_again = input("Play again? Y/N: ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break
    # Check for tie
    if board.is_tie():
        print("\n Tie game!\n")
        play_again = input("Play again? Y/N: ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    # Get O input
    o_choice = int(input("\nO) Please choose a space, 1-9: ")) - 1
    # Update board
    board.update_cell(o_choice, "O")
    refresh_screen()
    # Check for O win
    if board.is_winner("O"):
        print("\n O wins!\n")
        break
    
