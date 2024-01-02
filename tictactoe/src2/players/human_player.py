"""
Basic human player
"""
import numpy as np
from src2.players.base_player import Player

class HumanPlayer(Player):
    """
    Basic human player
    """
    def get_move(self, board: np.ndarray, player: int) -> list:
        """
        Console based move entry

        Returns:
            Union[int, int]: The move selected
        """
        while True:
            print("Type move in this format: i,j: ")
            move = input()

            # Validate
            move = move.replace(" ", "").replace(",", "")
            if len(move) > 2:
                print("Invalid format. Try again.")
            try:
                i, j = int(move[0]), int(move[1])
                return [i, j]
            except ValueError:
                print("Non-integer value entered. Try again.")
        