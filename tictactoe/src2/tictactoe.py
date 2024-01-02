"""
This module contains all the code necessary to play TicTacToe
"""
import numpy as np

from src2.players.base_player import Player

class TicTacToe:
    """
    This class creates and manages the TicTacToe Game
    """
    def __init__(self, size=3):
        self.size = size
        self.reset_board()

    def reset_board(self):
        """
        Replaces board with brand new one with all 0s
        """
        self.board = np.zeros(shape=(self.size,self.size), dtype=np.int8)

    def print_board(self):
        """
        Neatly prints out the game board
        """
        s = "---\n"
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                s += str(self.board[i, j])
            s += "\n"
        s += "---\n"
        print(s)

    def get_available_positions(self) -> list:
        """
        Gets a list of all available spaces on the board

        Returns:
            list: a list of (i,j) coordinates
        """
        available = []
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i, j] == 0:
                    available.append((i,j))
        return available

    def make_move(self, player_num: int, i: int, j: int):
        """
        Tries to mark player spot on the board

        Args:
            player_num (int): The player number
            i (int): i coordinate
            j (int): j coordinate
        """
        if player_num == 0:
            raise PlayerNumberException("Player number must be non-zero integer")
        if self.board[i, j] != 0:
            raise ValueError("Spot has already been taken")
        self.board[i, j] = player_num

    def get_players_on_board(self) -> np.ndarray:
        """
        Returns the numbers of each player on the board

        Returns:
            np.ndarray: The list of player numbers
        """
        return np.unique(self.board)

    def check_winner(self) -> int:
        """
        Checks to see if a player won

        Returns:
            int: who won (0 if no one)
        """
        players = self.get_players_on_board()
        tie = 0
        for p in players:
            # Check rows
            for i in range(len(self.board)):
                row = np.unique(self.board[i, :])
                if p in row and len(row) == 1:
                    return p
                if 1 in row and 2 in row:
                    tie += 1
            # Check colunns
            for j in range(len(self.board[0])):
                col = np.unique(self.board[:, j])
                if p in col and len(col) == 1:
                    return p
                if 1 in col and 2 in col:
                    tie += 1
            # Check diagonals
            d1 = np.unique(np.diagonal(self.board))
            d2 = np.unique(np.fliplr(self.board).diagonal())
            if (p in d1 and len(d1) == 1) or (p in d2 and len(d2) == 1):
                return p
            if (1 in d1 and 2 in d1) and (1 in d2 and 2 in d2) and (tie == 6):
                return -1
        return 0

    def play_game(self, players: list[Player]):
        """
        Runs the actual game

        Args:
            players (list): A list of player objects
        """
        # Game setup
        self.reset_board()
        winner = 0
        player = 0

        # Begin loop
        while winner == 0:
            # Make move
            self.print_board()
            print(f"Player {player+1} turn")
            while True:
                try:
                    i, j = players[player].get_move(self.board, player)
                    self.make_move(player + 1, i, j)
                    break
                except ValueError:
                    print("Spot already taken. Try again")
                except IndexError:
                    print("Bad coordinates. Try again")
            # Next round setup
            winner = self.check_winner()
            player = player + 1
            if player >= len(players):
                player = 0
        print("\nFinal board:")
        self.print_board()
        if winner == -1:
            print("Tie game!")
        else:
            print(f"Player {winner} wins!")

class PlayerNumberException(Exception):
    """
    Raised when the player number requested is not on the board
    """
