from copy import deepcopy
from game import *

def a_star(game, max_depth):
    queue = []
    visited_list = set()#we use set instead of lists (they are unordered, unindexed and have no duplicates)
    path = []
    depth = 0
    cost_t = game.cost + game.manhattan_distance()
    queue.append((cost_t, depth, game.game_board, game.pieces, path))
    visited_list.add(game.get_state_hashable()) #we are comparing strings instead of matrices
    while queue:
        queue.sort()
        _, current_depth, current_board, current_pieces, current_path = queue.pop(0) # Pop the node with the lowest total cost from the queue.
        new_game = Game(current_pieces, current_board)
        if new_game.win() == True:
            return current_path
        
        if current_depth < max_depth:
            for move in get_possible_moves(new_game):
                new_game_state = deepcopy(new_game)
                execute_moves(new_game_state, move) 
                if new_game_state.get_state_hashable() not in visited_list:
                    visited_list.add(new_game_state.get_state_hashable())
                    new_path = current_path + [move]
                    cost_t = new_game_state.manhattan_distance() + new_game_state.cost
                    queue.append((cost_t, current_depth +1, new_game_state.game_board, new_game_state.pieces, new_path ))
        else:
            return None
    return None

