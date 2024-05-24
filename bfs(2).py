from copy import deepcopy
from game import *

def breadth_first_search(game, max_depth):
    visited_list = set()
    queue = []
    path = []
    depth = 0
    queue.append((depth, game.game_board, game.pieces, path ))
    visited_list.add(game.get_state_hashable())
    while len(queue) != 0:
        current_depth, current_board, current_pieces, current_path = queue.pop(0)
        new_game = Game(current_pieces, current_board)
        if new_game.win() == True:
            return current_path
        if current_depth < max_depth:
            for move in get_possible_moves(new_game):
                new_game_state = deepcopy(new_game)
                execute_moves(new_game_state, move) 
                if new_game_state.game_board not in visited_list: 
                    visited_list.add(new_game_state.get_state_hashable())
                    new_path = current_path + [move]
                    queue.append((current_depth + 1, new_game_state.game_board, new_game_state.pieces, new_path ))
        else:
            return None
    return None