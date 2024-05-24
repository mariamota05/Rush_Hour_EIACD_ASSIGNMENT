from copy import deepcopy
from game import *

def greedy(game, max_depth):
    queue = []
    visited = []
    path = []
    depth = 0
    #Set the heuristic function
    queue.append(((game.manhattan_distance()), depth, game.game_board, game.pieces, path))
    visited.append(game.game_board)
    while len(queue) != 0:
        queue.sort()    
        _, current_depth, current_board, current_pieces, current_path = queue.pop(0)
        new_game = Game(current_pieces, current_board)

        if new_game.win() == True:
            return current_path
        if current_depth < max_depth:
            for move in get_possible_moves(new_game):
                new_game_state = deepcopy(new_game)
                execute_moves(new_game_state, move)
                if new_game_state.game_board not in visited:
                    visited.append(new_game_state.game_board)
                    new_path = current_path + [move]
                    queue.append((new_game_state.manhattan_distance(), current_depth +1, new_game_state.game_board, new_game_state.pieces, new_path ))
        else:
            return None
    return None