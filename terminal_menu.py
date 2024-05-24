from game import *
from rh_terminal import *
from board import board
import time
from levels import *

def start_terminal():
    print(" ________________________________")
    print("| Let's start!                   |")
    print("| Keybinds:                      |")
    print("| 'quit': End the game           |")
    print("| 'menu': Back to level choice.  |")
    print("| 'restart': Restart the level   |")
    print("| 'solve': auto-solver           |")
    print("|________________________________|")

    start = input("Are you ready? (yes/no) ")
    while start not in ['y','n','yes', 'no', 'Yes', 'No', 'quit', 'Quit']:
        print("Try again!")
        start = input("Are you ready? (yes/no) ")

    if start in ['n','no', 'No', 'quit','Quit']:
        print("")
        print("See ya!")
        quit()
    else:
        menu()


def menu():
    '''function to chose the difficulty'''
    difficulty_choice = choose_difficulty()

    if difficulty_choice in ['Easy', 'easy']:
        easy_mode()    
    elif difficulty_choice in ["Medium", "medium"]:
        medium_mode()
    elif difficulty_choice in ["Hard", "hard"]:
        hard_mode()
    elif difficulty_choice in ["Advanced", "advanced"]:
        advanced_mode()
    elif difficulty_choice in ["genius", "Genius"]:
        genius_mode()
    elif difficulty_choice in ["impossible", "Impossible"]:
        impossivel_mode()
    else:
        print("")
        print("See ya!")
        quit()


easy_levels = {
    '1': level1_pieces,
    '2': level2_pieces,
    '3': level3_pieces,
    '4': level4_pieces,
    '5': level5_pieces,
}

medium_levels = {
    '11': level11_pieces,
    '12': level12_pieces,
    '13': level13_pieces,
    '14': level14_pieces,
    '15': level15_pieces
}

hard_levels = {
    '21': level21_pieces,
    '22': level22_pieces,
    '23': level23_pieces,
    '24': level24_pieces,
    '25': level25_pieces
}

expert_levels = {
    '31': level31_pieces,
    '32': level32_pieces,
    '33': level33_pieces,
    '34': level34_pieces,
    '35': level35_pieces
}

genius_levels = {
    '46': level46_pieces,
    '47': level47_pieces,
    '48': level48_pieces,
    '49': level49_pieces,
    '50': level50_pieces
}

impossivel_level ={
    '100': level100_pieces
}

def choose_difficulty():
    print("")
    print("Menu:")
    print("Easy")
    print("Medium")
    print("Hard")
    print("Advanced")
    print("Genius")
    print("Impossible")
    print("")
    difficulty_input = input("Choose the level difficulty (exemple: Easy): ")
    while difficulty_input not in ['Easy', 'easy', 'Medium', 'medium', 'Hard', 'hard','genius','Genius','advanced','Advanced','Impossible','impossible','quit']:
        print("Try again!")
        difficulty_input = input("Choose the level difficulty (exemple: Easy): ")
    return difficulty_input


def easy_mode():
    print("")
    print("EASY:")
    print("*Level 1*")
    print("*Level 2*")
    print("*Level 3*")
    print("*Level 4*")
    print("*Level 5*")
    print("")
    level_input = input("Choose the level (Eg: 1): ")
    while level_input not in ['1', '2', '3', '4', '5', 'quit', 'Quit', 'menu', 'Menu']:
        print("Try again!")
        level_input = input("Choose the level (Eg: 1): ")

    if level_input == 'quit' or level_input == 'Quit':
        print("")
        print("See ya!")
        quit()

    elif level_input in ['menu', 'Menu']:
        menu() 

    else:
        stamp = True
        start_game_time = time.time()
        next = play_game_in_terminal(deepcopy(easy_levels[level_input]), board, stamp)
        end_game_time = time.time()
        total = end_game_time - start_game_time
        minutes1 = total //60
        seconds1 = total % 60
        print("The game took %d minutes e %d seconds" % (minutes1,seconds1))
        next
        menu()


def medium_mode():
    print("")
    print("MEDIUM:")
    print("*Level 11*")
    print("*Level 12*")
    print("*Level 13*")
    print("*Level 14*")
    print("*Level 15*")
    print("")
    level_input = input("Choose the level (Eg.: 11): ")
    while level_input not in ['11', '12', '13', '14', '15', 'quit', 'menu', 'Menu']:
            print("Try again!")
            level_input = input("Choose the level (Eg: 11): ")

    if level_input == 'quit':
        print("")
        print("See ya!")
        quit()
    elif level_input in ['menu', 'Menu']:
        menu()  
        
    else:
        stamp = True
        start_game_time = time.time()
        next = play_game_in_terminal(deepcopy(medium_levels[level_input]), board, stamp)
        end_game_time = time.time()
        total = end_game_time - start_game_time
        minutes2 = total //60
        seconds2 = total % 60
        print("The game took %d minutes e %d seconds" % (minutes2,seconds2))
        next
        menu()



def hard_mode():
    print("")
    print("HARD:")
    print("*Level 21*")
    print("*Level 22*")
    print("*Level 23*")
    print("*Level 24*")
    print("*Level 25*")
    print("")
    level_input = input("Choose the level (Eg.:1): ")
    while level_input not in ['21', '22', '23', '24', '25', 'quit', 'menu', 'Menu']:
            print("Try Again!")
            level_input = input("Choose the level (Eg.: 21): ")

    if level_input == 'quit':
        print("")
        print("See ya!")
        quit()
    elif level_input in ['menu', 'Menu']:
        menu()  
    else:
        stamp = True
        start_game_time = time.time()
        next = play_game_in_terminal(deepcopy(hard_levels[level_input]), board, stamp)
        end_game_time = time.time()
        total = end_game_time - start_game_time
        minutes3 = total //60
        seconds3 = total % 60
        print("The game took %d minutes e %d seconds" % (minutes3,seconds3))
        next
        menu()


def advanced_mode():
    print("")
    print("Advanced:")
    print("*Level 31*")
    print("*Level 32*")
    print("*Level 33*")
    print("*Level 34*")
    print("*Level 35*")
    print("")
    level_input = input("Choose the level (Eg: 31): ")
    while level_input not in ['31', '32', '33', '34', '35', 'quit', 'Quit', 'menu', 'Menu']:
        print("Try Again!")
        level_input = input("Choose the level (Eg: 31): ")

    if level_input == 'quit' or level_input == 'Quit':
        print("")
        print("See ya!")
        quit()

    elif level_input in ['menu', 'Menu']:
        menu() 

    else:
        stamp = True
        start_game_time = time.time()
        next = play_game_in_terminal(deepcopy(expert_levels[level_input]), board, stamp)
        end_game_time = time.time()
        total = end_game_time - start_game_time
        minutes4 = total //60
        seconds4 = total % 60
        print("The game took %d minutes e %d seconds" % (minutes4,seconds4))
        next
        menu()


def genius_mode():
    print("")
    print("Genius:")
    print("*Level 46*")
    print("*Level 47*")
    print("*Level 48*")
    print("*Level 49*")
    print("*Level 50*")
    print("")
    level_input = input("Choose the level (Eg: 46): ")
    while level_input not in ['46', '47', '48', '49', '50', 'quit', 'Quit', 'menu', 'Menu']:
        print("Try Again!")
        level_input = input("Choose the level (Eg: 46): ")

    if level_input == 'quit' or level_input == 'Quit':
        print("")
        print("See ya!")
        quit()

    elif level_input in ['menu', 'Menu']:
        menu() 

    else:
        stamp = True
        start_game_time = time.time()
        next = play_game_in_terminal(deepcopy(genius_levels[level_input]), board, stamp)
        end_game_time = time.time()
        total = end_game_time - start_game_time
        minutes5 = total //60
        seconds5 = total % 60
        print("The game took %d minutes e %d seconds" % (minutes5,seconds5))
        next
        menu()
    
def impossivel_mode():
    print("")
    print("Impossible:")
    print("*Level 100*")
    print("")
    level_input = input("Write '100': ")
    while level_input not in [ '100', 'quit', 'Quit', 'menu', 'Menu']:
        print("Try again!")
        level_input = input("Write '100'")

    if level_input == 'quit' or level_input == 'Quit':
        print("")
        print("See ya!")
        quit()

    elif level_input in ['menu', 'Menu']:
        menu() 

    else:
        stamp = True
        start_game_time = time.time()
        next = play_game_in_terminal(deepcopy(impossivel_level[level_input]), board, stamp)
        end_game_time = time.time()
        total = end_game_time - start_game_time
        minutes1 = total //60
        seconds1 = total % 60
        print("The game took %d minutes e %d seconds" % (minutes1,seconds1))
        next
        menu()


def next_level(level_input):
    if int(level_input) + 1 < 6:  #quando pusermos mais niveis temos de mudar
        new_level_input = str(int(level_input) + 1)
        next_level_input = input("Would you like to go to level" + str(new_level_input) + "?(y/n) ")
        while next_level_input not in ['y','yes','Yes', 'Y', 'n', 'N','no','No','quit']:
            print("Try again")
            next_level_input = input("Would you like to go to level" + str(new_level_input) + "?(y/n) ")

        if next_level_input == 'quit':
            print("")
            print("See ya!")
            quit()
        elif next_level_input in ['y','yes','Yes', 'Y']:
            return new_level_input
        else:
            menu()
    else:
        menu()



