from board import*
from game import *
from levels import *
from bfs import breadth_first_search
from a_star import a_star
from greedy import greedy



def algorthm_play(game, search_method, max_depth):
    if search_method == 'bfs':
            path = breadth_first_search(game, max_depth)
    elif search_method == 'a_star':
        path = a_star(game, max_depth)
    elif search_method == 'greedy':
        path = greedy(game, max_depth)
    return path

def choose_method(game):
    search_method = 'a_star'
    max_depth = 100
    n_hints = 1
    hint_input = input('The atual method is A*. Would you like to change it? (y/n) ')
    while hint_input not in ['y', 'Y', 'n', 'N']:
        print("Try again!")
        hint_input = input('Would you like to change it? (y/n) ')
    if hint_input in ['n', 'N']:
        get_hint(game, search_method, max_depth, n_hints)
    else:
        print("You can change to: 'bfs', 'a_star' or 'greedy'.")
        search_method = str(input("search method: "))
        while search_method not in ['bfs', 'a_star', 'greedy']:
            print("Try again!")
            search_method = str(input("search method: "))
        n_hints = 1             
        get_hint(game, search_method, max_depth, n_hints)


def get_hint(game, search_method, max_depth, n_hints):
    n = n_hints
    if search_method == 'bfs':
        path = breadth_first_search(game, max_depth)
        if path is not None:
            print("Resposta bfs: ", path[:n])
        else:
            print("Can't find any path!")
    elif search_method == 'a_star':
        path = a_star(game, max_depth)
        if path is not None:
            print("Resposta A*: ", path[:n])
        else:
            print("Can't find any path!")
    elif search_method == 'greedy':
        path = greedy(game, max_depth)
        if path is not None:
            print("Resposta greedy: ", path[:n])
        else:
            print("Can't find any path!")

def play_game_in_terminal(pieces, board, stamp):
    level_pieces = deepcopy(pieces)
    game_board = create_rush_hour_board(level_pieces, board)
    game = Game(level_pieces, game_board)
    game.print_game()
    num_hints = 0
    game_piece_id = []
    for piece_id in level_pieces:
        game_piece_id.append(piece_id)
    game_direction = ['up', 'down', 'left', 'right']
    search_method = 'a_star'
    list= algorthm_play(game, search_method, 100)
    break_point = False
    while game.win() == False:
        move_input = input("Which piece wold you like to move(eg: 1 up)? ")
        move_input = move_input.split()
        list_move_input = []
        for word in move_input:
            list_move_input.append(word)

        if len(list_move_input) == None:
            print("Try again!")
        elif len(list_move_input) == 1:
            if list_move_input[0] == 'quit':
                print("")
                print("See ya!")
                quit()
            elif list_move_input[0] in ['menu', 'Menu']:
                return False
            elif list_move_input[0] == 'hint':
                choose_method(game)
                num_hints += 1
            elif list_move_input[0] == 'restart':
                level_pieces = deepcopy(pieces)
                game_board = create_rush_hour_board(level_pieces, board)
                game = Game(level_pieces, game_board)
                game.print_game()
            elif list_move_input[0] == 'solve':
                search_method = 'a_star'
                list= algorthm_play(game, search_method, 100)
                if list != None:
                    for x in list:
                        print(x)
                else:
                    print("No solution found")
                break_point = True
            else:
                print("Try again!")
        elif len(list_move_input) == 2:
            piece_id = move_input[0]
            direction = move_input[1]
            if (piece_id in game_piece_id) and (direction in game_direction):
                game.move_pieces(piece_id, direction, stamp)
            else:
                print("Try again!")
        else:
            print("Try again!")
        if break_point == True:
            break
    if break_point == False:
        print("You used %d hints" % (num_hints))
        if list != None:
            print("The a_star algorithm used %d moves" % (len(list)))
    return True