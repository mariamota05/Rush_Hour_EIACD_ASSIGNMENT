# Rush_Hour_EIACD_ASSIGNMENT
Work assignment 1º Year 1º Semester - EIACD. Work made by me and my colleagues https://github.com/Dianassp05 and https://github.com/Galmass

How to run:
---

Access the terminal and make sure you are in the directory containing the game to access it.
Run the command 'python3 rushhour.py' and choose whether you want to play the game in Pygame or in the terminal.
```
python3 rushhour.py
```
Select the desired difficulty, choose a level and have fun.


Requirements:
---

Python;
Libraries Pygame, Sys, Copy.


How to play:
---


The goal of the game is to move the red car "p" the right most tile of the board.
The cars can only move forward and backward in the direction they face and no car is able to go through any other car.
To move the cars in the pygame version press the key with the car's name you wish to move then use the arrows on the keyboard. If the location you want the car to move to is a valid location it will be moved, otherwise the car will remain in place.
In the terminal version of the game type the name of the car and the direction you wish to move and press enter, for example: 6 up. If this is a valid move the screen will update and the cars new location will be show.


Information:
---

At any moment you can reset the level, ask for hints or have artificial intelligence resolve the level. In the pygame version we use A* and in the terminal version there is the option to use BFS and greedy too.
