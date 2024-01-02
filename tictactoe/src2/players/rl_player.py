"""
Q-Learning Policy Based Player
"""
import numpy as np
from src2.players.base_player import Player

class RLPlayer(Player):
    """
    Q-Learner
    """
    def __init__(self):
        self.reset_policy()

    def reset_policy(self):
        """
        There are 9 board spots
        There are 3 possible states. (0=None, 1=Player, 2=Opponent)
        That makes for a total of 9^3 = 729 spots
        """
        self.policy = np.zeros(shape=(3, 3, 3, 3, 3, 3, 3, 3, 3, 2))

    def get_current_state_index(self, board: np.ndarray, player_num: int) -> list:
        """
        Gets the index of the policy
        """
        index = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i, j] == 0:
                    index.append(0)
                elif board[i, j] == player_num:
                    index.append(1)
                else:
                    index.append(2)
        return index

    def get_move(self, board: np.ndarray, player: int) -> list:
        """
        Based on current state of the environment, selects action (i, j)

        Returns:
            list: (i,j)
        """
        idx = self.get_current_state_index(board, player)
    #     return (self.policy[idx + [0]], self.policy[idx + [1]])
    
    # state
    # actions
    # rewards (state + action -> new_state)
    
