from xmlrpclib import ServerProxy

from board import Board
from AI import OneLevelAI

game_server = ServerProxy("http://localhost:8006")
game_id = game_server.start_game()

ai = OneLevelAI()

while True:
    board = Board(game_server.get_board_state(game_id))
    board.pprint()
    x, y = ai.get_best_move(board, 1)
    
    state = game_server.move(x, y, game_id)
    board = Board(game_server.get_board_state(game_id))
    board.pprint()
    print state
    if state[1] == 'game_over':
        break

print 'exiting'
