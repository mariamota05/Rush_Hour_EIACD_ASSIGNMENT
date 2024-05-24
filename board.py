from copy import deepcopy
board = [
    ['*', '_', '_', '_', '_', '_', '_', '*'],
    ['|', '0', '0', '0', '0', '0', '0', '|'],
    ['|', '0', '0', '0', '0', '0', '0', '|'],
    ['|', '0', '0', '0', '0', '0', '0', ':'],
    ['|', '0', '0', '0', '0', '0', '0', '|'],
    ['|', '0', '0', '0', '0', '0', '0', '|'],
    ['|', '0', '0', '0', '0', '0', '0', '|'],
    ['*', '_', '_', '_', '_', '_', '_', '*']
    ]


def create_rush_hour_board(pieces, game_board): #To prevent making changes to the original board
    game_board = deepcopy(board)
    
    for piece_id in pieces:
        for position in pieces[piece_id]:   # 'piece_id' : [...],[...]
            position_x = position[0]
            position_y = position[1]
            if game_board[position_x][position_y] == '0':
                game_board[position_x][position_y] = piece_id

    return (game_board)