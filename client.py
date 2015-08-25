from xmlrpclib import ServerProxy

from board import Board
from AI import ReversiSimpleAI

game_server = ServerProxy("http://127.0.0.1:8006")
game_id = game_server.start_game('vasya@gmail.com')

ai = ReversiSimpleAI()

step = 0
while True:
    print '==============================='
    board = Board(game_server.get_board_state(game_id))
    board.pprint()

    x, y = ai.get_best_move(board, 1)
    
    state = game_server.move(x, y, game_id)

    step += 1

    board = Board(game_server.get_board_state(game_id))
    print '_______________________________'
    board.pprint()
    print state
    if state[1] == 'game_over':
        if board.score(1) > board.score(2):
            print "YOU'VE WON!!!", 'in ', step, 'steps'
        if board.score(1) == board.score(2):
            print 'EQUAL SCORE', 'in ', step, 'steps'
        if board.score(1) < board.score(2):
            print "YOU'VE LOST", 'in ', step, 'steps'
        
        print 'SCORE', board.score(1), board.score(2)
        break

print 'exiting'
