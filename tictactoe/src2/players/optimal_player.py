"""
Optimal player
"""
import random
import numpy as np
from src2.players.base_player import Player

class OptimalPlayer(Player):
    turns = 0
    corner = [[0, 0], [0, 2], [2, 0], [2, 2]]
    middle = [1, 1]
    edge = [[0, 1], [1, 0], [2, 1], [1, 2]]
    """
    Optimal player
    """
    def first_player_play(self, board: np.ndarray) -> list:
        if self.turns == 0:
            return random.choice(self.corner)
        if self.turns == 1:
            if board[1, 1] != 0:
                return random.choice(self.corner)
            return [1, 1]
        return [-1, -1]

    def second_player_play(self, board: np.ndarray) -> list:
        if self.turns == 0:
            if board[1,1] != 0:
                return random.choice(self.corner)
            else:
                return self.middle
        return [-1, -1]

    def get_move(self, board: np.ndarray, player: int) -> list:
        """
        Console based move entry

        Returns:
            Union[int, int]: The move selected
        """
        if player == 0:
            move = self.first_player_play(board)
        else:
            move = self.second_player_play(board)
        self.turns += 1
        return move
