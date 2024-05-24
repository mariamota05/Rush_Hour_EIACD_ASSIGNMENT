class Game(): 
    def __init__(self, pieces, game_board):
        self.game_board = game_board
        self.pieces = pieces
        self.cost = 0


    def print_game(self):
        for row in self.game_board:
            print(' '.join(row))


    def valid_move(self, piece_id, new_piece_coordinates):

        piece_coordenates = self.pieces[piece_id]
        orientacao = 1 # "horizontal"
        primeiro_elemento = piece_coordenates[0][0]
        for coordenadas in piece_coordenates[1:]:  
            if coordenadas[0] != primeiro_elemento:
                orientacao = 0

        for i in range(len(piece_coordenates)):
            if orientacao == 1 :
                if (new_piece_coordinates[0][0] - piece_coordenates[0][0]) != 0 :
                    return 'not valid'
            else:
                if (new_piece_coordinates[0][1] - piece_coordenates[0][1]) != 0 :
                    return 'not valid'
        
        all_moves = ['valid' if self.game_board[new_coords[0]][new_coords[1]] in ['0', piece_id] else 'not valid' for new_coords in new_piece_coordinates]
        if 'not valid' in all_moves:
            return 'not valid'
        else:
            return 'valid'

    def get_state_hashable(self):
        s=""
        grid=self.game_board
        for i in range(6):
            for j in range(6):
                s+="{}".format(grid[i+1][j+1])
        return s
    
    def update_game_board(self, piece_id, new_piece_coordinates):
        for position in self.pieces[piece_id]:
            position_x = position[0]
            position_y = position[1]
            self.game_board[position_x][position_y] = '0'

        for new_coordinate in new_piece_coordinates:
            new_coordinate_x = new_coordinate[0]
            new_coordinate_y = new_coordinate[1]
            self.game_board[new_coordinate_x][new_coordinate_y] = piece_id


    def update_pieces_coordinates(self, piece_id, new_piece_coordinates):
        new_list = []
        for new_coordinate in new_piece_coordinates:
            new_list.append(new_coordinate)
        self.pieces[piece_id] = new_list


    def pieces_movements(self, piece_id, direction):
        piece_coordenates = self.pieces[piece_id]
        if direction == 'up':
            move_x, move_y = -1, 0
        elif direction == 'down':
            move_x, move_y = 1, 0
        elif direction == 'left':
            move_x, move_y = 0, -1
        elif direction == 'right':
            move_x, move_y = 0, 1
        new_piece_coordenates = []
        for coordenates in piece_coordenates:  
            new_x = coordenates[0] + move_x
            new_y = coordenates[1] + move_y
            new_piece_coordenates.append((new_x, new_y))
        
        return new_piece_coordenates
        

    def move_pieces(self, piece_id, direction, stamp):  
        new_piece_coordenates = self.pieces_movements(piece_id, direction)

        if self.valid_move(piece_id, new_piece_coordenates) == 'valid':
            self.update_game_board(piece_id, new_piece_coordenates)
            self.update_pieces_coordinates(piece_id, new_piece_coordenates)
            self.cost += 1
            if stamp == True:
                self.print_game()
            if (self.win() == True) and (stamp == True):
                print(" __   __                                 _  _  _")
                print(" \\ \\ / /                                | || || |")
                print("  \\ v /___ _  _    __  _  __ ___  _ __  | || || |")
                print("   | |/ _ \\ || |   \\ \\/ \\/ // _ \\| '  \\ |_||_||_|")
                print(r"   |_|\___/\_,_|    \_/ \_/ \___/|_||_| (_)(_)(_)")
                print("You used %d moves" % (self.cost))
        else:
            if stamp == True:
                print("You can't do this move!!")
                self.print_game()
            else:
                pass

    #heuristic
    def manhattan_distance(self):
            piece_id = 'p'
            piece_coordinates = self.pieces[piece_id]
            winning_location = [(3,5),(3,6)]
            current_distance = -1

            for coordinate in piece_coordinates:
                distances = []
                for win_coordinate in winning_location:
                    distance = abs(coordinate[0] - win_coordinate[0]) + abs(coordinate[1] - win_coordinate[1])
                    distances.append(distance)
                min_distance = min(distances)

                if current_distance < min_distance:
                    current_distance = min_distance

            cost_h = current_distance
            
            return cost_h

    def count_blocking_vehicles(self):
        target_row = 3
        target_car_end_position = max([pos[1] for pos in self.pieces['p'] if pos[0] == target_row])
        blocking_vehicles = set()
        
        # We scan from just past the rightmost position of 'p' to the exit column 5
        for col in range(target_car_end_position + 1, 6):
            if self.game_board[target_row][col] != '0' and self.game_board[target_row][col] not in {'*', '|', ':'}:
                blocking_vehicles.add(self.game_board[target_row][col])
        
        return len(blocking_vehicles)

    def win(self):
        winning_location = [(3,5),(3,6)]
        counter = 0
        for position in self.pieces['p']:
            if position in winning_location:
                counter += 1

        if counter == 2:
            return True
        else:
            return False
    

def get_possible_moves(new_game):
    # Get all possible moves for the current game state
    possible_moves = []
    for piece_id in new_game.pieces:
        for direction in ['up', 'down', 'left', 'right']:
            new_piece_coordenates = new_game.pieces_movements(piece_id, direction)
            if new_game.valid_move(piece_id, new_piece_coordenates) == 'valid':
                possible_moves.append((piece_id, direction))
    
    return possible_moves

def execute_moves(new_game, move):
    piece_id = move[0]
    direction = move[1]
    new_piece_coordenates = new_game.pieces_movements(piece_id, direction)
    new_game.update_game_board(piece_id, new_piece_coordenates)
    new_game.update_pieces_coordinates(piece_id, new_piece_coordenates)
    new_game.cost += 1

