"""
Random player
"""
import random
import numpy as np
from src2.players.base_player import Player

class RandomPlayer(Player):
    """
    Random player
    """
    def get_move(self, board: np.ndarray, player: int) -> list:
        """
        Console based move entry

        Returns:
            Union[int, int]: The move selected
        """
        available = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i,j] == 0:
                    available.append((i,j))
        return random.choice(available)
