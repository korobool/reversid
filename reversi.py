from SimpleXMLRPCServer import SimpleXMLRPCServer

from board import Board
from AI import OneLevelAI
import uuid
import pymongo

initial_state = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 2, 0, 0, 0],
                 [0, 0, 0, 2, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]


class ServerClass():
    def __init__(self):
        self._conn = pymongo.Connection('localhost', 27017)
        pass

    def start_game(self):
        id = uuid.uuid4()
        reversi = self._conn.reversi
        games = reversi.games
        games.insert({'game': str(id), 'board': initial_state})

        return str(id)

    def get_board_state(self, game_id):
        reversi = self._conn.reversi
        games = reversi.games
        game = games.find_one({"game": game_id})
        return game[u'board']

    def move(self, r, c, game_id):
        reversi = self._conn.reversi
        games = reversi.games
        game = games.find_one({"game": game_id})
        board = Board(game[u'board'])
        board = board.move(r, c, 1)

        ai = OneLevelAI()

        x, y = ai.get_best_move(board, 2)
        board = board.move(x, y, 2)

        games.update({'_id': game['_id']}, {"$set": {'board': board._internal_state}},
                     upsert=False)

        return True


server = SimpleXMLRPCServer(("", 8001))
server.register_instance(ServerClass())
server.serve_forever()