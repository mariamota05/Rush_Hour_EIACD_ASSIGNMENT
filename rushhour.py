from terminal_menu import * 

def start():
    print("Here is our interpretation of the 'Rush Hour Game' by 'ThinkFun'")
    print("Where do you want to play:")  
    print("*Terminal*")
    print("*Pygame*")
    print("*Quit*")
    choice = input("Please choose (Eg.: 'Terminal'): ")

    while choice.lower() not in ['terminal', 'pygame', 'quit']:
        print("Wrong input.")
        choice = input("Please choose (Eg.: 'Terminal'): ")

    if choice.lower() == 'quit':
        exit()
    elif choice.lower() == 'pygame':
        import visuals_pygame
        visuals_pygame.main()
    else:
        start_terminal()

if __name__ == '__main__':
    start()
