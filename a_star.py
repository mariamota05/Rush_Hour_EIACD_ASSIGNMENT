from copy import deepcopy
from game import *

def a_star(game, max_depth):
    queue = []
    visited_list = []
    path = []
    depth = 0
    # Set the total cost according to h(n)+g(n)
    cost_t = game.cost + game.manhattan_distance()
    queue.append((cost_t, depth, game.game_board, game.pieces, path))
    visited_list.append(game.game_board)
    while len(queue) != 0:
        queue.sort()
        _, current_depth, current_board, current_pieces, current_path = queue.pop(0) # Pop the node with the lowest total cost from the queue.
        new_game = Game(current_pieces, current_board)
        if new_game.win() == True:
            return current_path
        
        if current_depth < max_depth:
            for move in get_possible_moves(new_game):
                new_game_state = deepcopy(new_game)
                execute_moves(new_game_state, move) # Execute the move and update the game state
                if new_game_state.game_board not in visited_list: #avoiding loops
                    visited_list.append(new_game_state.game_board)
                    new_path = current_path + [move]
                    cost_t = new_game_state.manhattan_distance() + new_game_state.cost
                    queue.append((cost_t, current_depth +1, new_game_state.game_board, new_game_state.pieces, new_path ))
        else:
            return None
    
    return None
