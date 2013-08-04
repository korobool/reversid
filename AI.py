from random import choice


class ReversiAI():
    def get_best_move(self, board, current_player, Depth=2):
        return choice(board.possible_moves(current_player))


class OneLevelAI(ReversiAI):
    def get_best_move(self, board, current_player, Depth=2):
        return choice(board.possible_moves(current_player))