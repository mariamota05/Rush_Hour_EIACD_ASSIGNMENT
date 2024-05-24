import pygame
import sys
import os
from levels import *
from a_star import *
from bfs import *
from greedy import *
import copy
from board import *

# Initialize Pygame
pygame.init()

#set up constants
CELL_SIZE = 100
BOARD_SIZE = 6
WINDOW_SIZE = CELL_SIZE * BOARD_SIZE

BACKGROUND_COLOR = (255, 255, 255)
CAR_COLORS = {
    '1': (0, 255, 0),
    '2': (255, 0, 255),
    '3': (0, 0, 255),
    '4': (255, 255, 0),
    '5': (255, 128, 64),
    '6': (0, 128, 128),
    '7': (128, 128, 255),
    '8': (0, 0, 102),  
    '9': (153, 102, 51),
    'a': (255, 80, 80),
    'b': (230, 184, 0),
    'c': (51, 102, 0),
    'd': (204,102,153),
    'e': (128, 128, 0),
    'f': (0, 255, 255),
    'g': (255, 102, 0),
    'i': (255, 204, 51),
    'p': (255, 0, 0),
}

current_level = {}

font = pygame.font.Font(None, 36)
message_font = pygame.font.Font(None, 72) 
no_solution_font = pygame.font.Font(None, 72)

#buttom classe
class Button:
    def __init__(self,text, x, y, width, height, color):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        x, y = pos
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)


screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('Rush Hour Game')

FPS = 60  
clock = pygame.time.Clock()

def load_levels():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    levels_file = os.path.join(current_directory, 'levels.py')
    if not os.path.exists(levels_file):
        return {}
    try:
        levels = {}
        exec(open(levels_file).read(), {}, levels)  
        levels_rush = {key.lower(): value for key, value in levels.get('levels_rush', {}).items()}
        return levels_rush
    except Exception as e:
        print("Unable to load the follow levels:", e)
        return {}

levels = load_levels()

def setup_level(difficulty,level_number):
    global current_level, initial_state
    current_level = levels_rush[difficulty][int(level_number)]
    initial_state = copy.deepcopy(current_level)

def is_move_valid(car, new_positions):
    for pos in new_positions:
        if pos[0] < 1 or pos[0] > BOARD_SIZE or pos[1] < 1 or pos[1] > BOARD_SIZE:
            return False
    for other_car, positions in current_level.items():
        if other_car != car:
            for pos in new_positions:
                if pos in positions:
                    return False
    return True

def draw_board():
    screen.fill(BACKGROUND_COLOR)
    for x in range(0, WINDOW_SIZE, CELL_SIZE):
        for y in range(0, WINDOW_SIZE, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, BACKGROUND_COLOR, rect, 1)

def draw_cars():
    for car, positions in current_level.items():
        for position in positions:
            x = (position[1] - 1) * CELL_SIZE
            y = (position[0] - 1) * CELL_SIZE
            pygame.draw.rect(screen, CAR_COLORS[car], (x, y, CELL_SIZE, CELL_SIZE))
            text_surface = font.render(car, True, (0, 0, 0))
            screen.blit(text_surface, (x + CELL_SIZE // 4, y + CELL_SIZE // 4))

def check_victory():
    winning_positions = [(3, 5), (3, 6)]
    return all(pos in current_level['p'] for pos in winning_positions)
 
def choose_difficulty():
    screen.fill(BACKGROUND_COLOR)
    menu_dif_image = pygame.image.load("images/menu_dif.png")

    buttons = []
    difficulties = ['easy', 'medium', 'hard', 'advanced', 'genius', 'impossible']
    for i, difficulty in enumerate(difficulties):
        button = Button(difficulty, 200, 100 + i*60, 200, 50, (210, 180, 140),)
        buttons.append(button)

    back_button = Button("Back to Menu", 50, 500, 200, 50, (255, 102, 0))
    buttons.append(back_button)

    screen.blit((menu_dif_image), (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.is_clicked(pygame.mouse.get_pos()):
                        if button.text == "Back to Menu":  
                            return "back"  # back to main menu
                        if button.text == "easy": 
                            return "easy"
                        if button.text == "hard":  
                            return "hard"
                        if button.text == "medium":  
                            return "medium"
                        if button.text == "advanced":  
                            return "advanced"
                        if button.text == "genius":  
                            return "genius"
                        if button.text == "impossible":  
                            return "impossible"
        for button in buttons:
            button.draw(screen)
        pygame.display.flip()

def choose_level(difficulty):
    difficulty = difficulty.lower()
    screen.fill(BACKGROUND_COLOR)
    menu_levels = pygame.image.load("images/menu_levels.png")
    
    level_buttons = []
    levels = range(1, len(levels_rush[difficulty]) + 1)
    for i, level in enumerate(levels):
        level_button = Button(f"Level {level}", 200, 100 + i*60, 200, 50, (210, 180, 140),)
        level_buttons.append(level_button)
    
    screen.blit((menu_levels), (0, 0))

    back_to_difficulty_button = Button("Back to Difficulty", 50, 500, 200, 50, (255, 102, 0))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, button in enumerate(level_buttons):
                    if button.is_clicked(pygame.mouse.get_pos()):
                        return str(i + 1)  
                if back_to_difficulty_button.is_clicked(pygame.mouse.get_pos()):
                    return 'back' 
        for button in level_buttons:
            button.draw(screen)
        back_to_difficulty_button.draw(screen)
        pygame.display.flip()

def main_menu():
    pygame.init()
    screen.fill(BACKGROUND_COLOR)

    background_image = pygame.image.load("images/menu_background.png")

    buttons = [
        Button("Start", 350, 200, 200, 50, (255, 215, 0)),
        Button("Help", 350, 300, 200, 50, (255, 215, 0)),
        Button("Quit", 350, 400, 200, 50, (255, 215, 0))
    ]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.is_clicked(pygame.mouse.get_pos()):
                        if button.text == "Start":
                            return
                        elif button.text == "Help":
                            if how_to_play() == 'back':
                                screen.fill(BACKGROUND_COLOR)
                                continue
                        elif button.text == "Quit": 
                            pygame.quit()
                            sys.exit()
        screen.blit(background_image, (0, 0))
        
        for button in buttons:
            button.draw(screen)

        font_creators = pygame.font.Font(None, 26)
        creator1_text = "Diana Pereira up202304476"
        creator2_text = "Gonçalo Almas up202303768"
        creator3_text = "Maria Mota up202306707"
        text1_surface = font_creators.render(creator1_text, True, (255, 255, 153))
        screen.blit(text1_surface, (340, 520))  
        text2_surface = font_creators.render(creator2_text, True, (255, 255, 153))
        screen.blit(text2_surface, (340, 540))  
        text3_surface = font_creators.render(creator3_text, True, (255, 255, 153))
        screen.blit(text3_surface, (340, 560))  

        pygame.display.flip()
    

def game_loop():
    selected_car = None
    running = True
    clock.tick(FPS)
    global show_return_button
    return_button = Button("Menu", 150, 400, 200, 50, (0, 0, 0))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move_selected_car('up', selected_car)
                elif event.key == pygame.K_DOWN:
                    move_selected_car('down', selected_car)
                elif event.key == pygame.K_LEFT:
                    move_selected_car('left', selected_car)
                elif event.key == pygame.K_RIGHT:
                    move_selected_car('right', selected_car)
                elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                    car_id = str(event.key - pygame.K_0)
                    if car_id in current_level:
                        selected_car = car_id
                elif (event.key >= pygame.K_a and event.key <= pygame.K_g) or event.key == pygame.K_p or event.key == pygame.K_i:
                    car_id = chr(event.key)
                    if car_id in current_level:
                        selected_car = car_id
                elif event.key == pygame.K_r:
                    reset_level()
                elif event.key == pygame.K_q:
                    running = False
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_h:
                    font = pygame.font.Font(None, 36)
                    game_board = create_rush_hour_board(current_level, board)
                    game = Game(current_level, game_board)
                    display_hint(font, game)
                elif event.key == pygame.K_m:
                    return2_button = Button("Menu", 200, 300, 200, 50, (128, 0, 0))
                    return2_button.draw(screen)
                    pygame.display.update()
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running = False
                                pygame.quit()
                                sys.exit()
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                if return2_button.is_clicked(pygame.mouse.get_pos()):
                                    return 'back'
                elif event.key == pygame.K_s:
                    game_board = create_rush_hour_board(current_level, board)
                    game = Game(current_level, game_board)
                    moves = algorthm_play(game,'a_star',100)
                    if moves != None:
                        visualize_path(moves)
                    else:
                        message = no_solution_font.render("No solution found!", True, (0, 0, 0))
                        screen.blit(message, (WINDOW_SIZE // 2- 200, WINDOW_SIZE // 2-150 ))
                        pygame.display.update()
                        pygame.time.wait(500)
                    return_menu_button = Button("Menu", 200, 300, 200, 50, (128, 0, 0))
                    return_menu_button.draw(screen)
                    pygame.display.update()
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running = False
                                pygame.quit()
                                sys.exit()
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                if return_menu_button.is_clicked(pygame.mouse.get_pos()):
                                    return 'back'
        draw_board()
        draw_cars()
        if check_victory():
            victory_message = message_font.render("Victory!", True, (255, 0, 0))
            screen.blit(victory_message, (WINDOW_SIZE // 2 - 100, WINDOW_SIZE // 2 - 50))
            pygame.display.update()
            return_button = Button("Menu", 200, 300, 200, 50, (255, 102, 0))
            return_button.draw(screen)
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if return_button.is_clicked(pygame.mouse.get_pos()):
                            return
       
        pygame.display.update()


def display_hint(font,game):
    moves = algorthm_play(game, 'a_star', 100)
    if moves:
        hint_message = font.render(f"Next move: {moves[0]}", True, (0, 0, 0))
        screen.blit(hint_message, (WINDOW_SIZE // 2 - 100, WINDOW_SIZE // 2))
        pygame.display.update()
        pygame.time.delay(2000)
    else:
        # No solution found
        hint_message = font.render("No solution found!", True, (0, 0, 0))
        screen.blit(hint_message, (WINDOW_SIZE // 2 - 150, WINDOW_SIZE // 2))
        pygame.display.update()
        pygame.time.delay(2000)

def reset_level():
    global current_level
    current_level = copy.deepcopy(initial_state)


def move_selected_car(direction, selected_car):
    if selected_car:
            car_positions = current_level[selected_car]
            new_positions = car_positions.copy()

            if car_positions[0][1] == car_positions[1][1]:  # Vertical car
                if direction in ['up', 'down']:
                    
                    if direction == 'up':
                        if all(pos[0] > 1 for pos in car_positions):
                            new_positions = [(pos[0] - 1, pos[1]) for pos in new_positions]
                    elif direction == 'down':
                        if all(pos[0] < BOARD_SIZE for pos in car_positions): 
                            new_positions = [(pos[0] + 1, pos[1]) for pos in new_positions]
            else:  # Horizontal car
                if direction in ['left', 'right']:
                    if direction == 'left':
                        if all(pos[1] > 1 for pos in car_positions):
                            new_positions = [(pos[0], pos[1] - 1) for pos in new_positions]
                    elif direction == 'right':
                        if all(pos[1] < BOARD_SIZE for pos in car_positions): 
                            new_positions = [(pos[0], pos[1] + 1) for pos in new_positions]
            if is_move_valid(selected_car, new_positions):
                current_level[selected_car] = new_positions



def algorthm_play(game, search_method, max_depth):
    if search_method == 'bfs':
        path = breadth_first_search(game, max_depth)
    elif search_method == 'a_star':
        path = a_star(game, max_depth)
    elif search_method == 'greedy':
        path = greedy(game, max_depth)
    return path

def visualize_path(moves):
    for piece_id, direction in moves:
        move_selected_car(direction, piece_id)
        draw_board()
        draw_cars()
        pygame.display.update()
        pygame.time.delay(300) 

def how_to_play():
    pygame.init()
    how_to_play_screen = pygame.display.set_mode((600, 600)) 
    how_to_play_screen.fill(BACKGROUND_COLOR) 

    instructions = [
        "Instructions:",
        "- Press 'R' to reset the level.",
        "- Press 'Q' to quit the game at any time.",
        "- Press 'S' to solve.",
        "- Press 'M' to back to the levels menu",
        "- Press 'H' to ask for a hint",
        " ",
        "Controls:",
        "- To move a car, select it by pressing the number key",
        "  and then press the arrow key to move it.",
        "       For example, to move car 1 to the right,",
        "       select '1' and press the right arrow key ( > )."
    ]

    font = pygame.font.Font(None, 24) 
    y = 50 

    for instruction in instructions:
        text_surface = font.render(instruction, True, (0, 0, 0))  
        how_to_play_screen.blit(text_surface, (20, y)) 
        y += 30

    back_button = Button("Menu", 450, 350, 120, 40, (128, 0, 0))

    pygame.display.flip()  

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  
                return 'back'  #back to the main menu
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.is_clicked(event.pos):
                    return 'back'  

        back_button.draw(how_to_play_screen)
        pygame.display.flip()


def main():
    while True:
        a = main_menu()
        if a == 'how':
            how_to_play()
        else: 
            while True:
                difficulty = choose_difficulty()
                if difficulty == 'back':
                    break  
                while True:
                    level_number = choose_level(difficulty)
                    if level_number == 'back':
                        break
                    elif level_number == 'quit':
                        return  
                    else:
                        setup_level(difficulty, int(level_number) - 1)
                        game_loop()



if __name__ == "__main__":
    difficulty = choose_difficulty()
    while difficulty != 'quit':
        level_number = choose_level(difficulty)
        if level_number and int(level_number) <= len(levels_rush[difficulty]):
            setup_level(difficulty, int(level_number) - 1)
            game_loop()
        else:
            print("Invalid level! Please try again.")
        difficulty = choose_difficulty()