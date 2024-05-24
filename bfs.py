from copy import deepcopy
from game import *

def breadth_first_search(game, max_depth):
    visited_list = []
    queue = []
    path = []
    depth = 0
    queue.append((depth, game.game_board, game.pieces, path ))
    visited_list.append(game.game_board)
    while len(queue) != 0:
        current_depth, current_board, current_pieces, current_path = queue.pop(0)
        new_game = Game(current_pieces, current_board)
        if new_game.win() == True:
            return current_path
        if current_depth < max_depth:
            for move in get_possible_moves(new_game):
                new_game_state = deepcopy(new_game)
                execute_moves(new_game_state, move)  # Execute the move and update the game state.
                if new_game_state.game_board not in visited_list: # If the state has not been visited, add it to the queue along with its depth, game board, pieces, and path.
                    visited_list.append(new_game_state.game_board)
                    new_path = current_path + [move]
                    queue.append((current_depth + 1, new_game_state.game_board, new_game_state.pieces, new_path ))
        else:
            return None
    return None