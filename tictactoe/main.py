"""
Main
"""
from src2.players.human_player import HumanPlayer
from src2.players.random_player import RandomPlayer
from src2.tictactoe import TicTacToe

def main():
    """
    Runs a basic game
    """
    p1 = RandomPlayer()
    p2 = RandomPlayer()
    game = TicTacToe()
    game.play_game([p1, p2])

if __name__ == "__main__":
    main()
