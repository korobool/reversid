from board import Board
from AI import ReversiAI, OneLevelAI

initial_state = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 2, 0, 0, 0],
                [0, 0, 0, 2, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]

board = Board(initial_state)

ai = OneLevelAI()
current_player = 1

steps = 0
while board.has_moves(current_player):

    x, y = ai.get_best_move(board, current_player, Depth=4 - current_player)

    print('move:', steps, 'player:', current_player, 'action', (x, y))

    board = board.move(x, y, current_player)

    board.pprint()
    steps += 1
    # take a next player
    current_player = current_player % 2 + 1

print 'The End', 'SCORE 1:', board.score(1),'SCORE 2:', board.score(2)