"""
Basic player type
"""
from abc import ABC, abstractmethod
import numpy as np

class Player(ABC):
    """
    Basic player type
    """
    @abstractmethod
    def get_move(self, board: np.ndarray, player: int) -> list:
        """
        Should get the list of coordiates that the player wants to move

        Returns:
            list: (i, j)
        """
        return [0, 0]
