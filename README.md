# Rabbit and Carrot Game

## Overview

This is a command-line game where you control a rabbit that needs to collect carrots and reach rabbit holes to win.

## How to Play

1. **Running the Game**

   - To run the game, execute the `rabbit_carrot_game.py` script in your terminal or command prompt:

     ```shell
     python rabbit_carrot_game.py
     ```

2. **Setting Up the Game**

   - Enter the following information to set up the game:
     - Map grid size (e.g., 5 for a 5x5 grid).
     - Number of carrots to place on the map.
     - Number of rabbit holes to place on the map.

3. **Game Controls**

   - The game will start, and you will see the initial game map displayed in the console.
   - Use the following controls to navigate the rabbit:
     - Use 'w', 'a', 's', and 'd' to move the rabbit up, left, down, and right, respectively.
     - Use 'p' to pick up a carrot if the rabbit is on a carrot cell. Once picked up, the rabbit will carry the carrot.
     - Use 'j' to jump over rabbit holes if the rabbit is adjacent to a hole (rabbit holes are represented by 'O'). To win the game, the rabbit must jump over rabbit holes while carrying a carrot and reach the rabbit hole cell.

4. **Winning the Game**

   - To win the game, follow these steps:
     - Make sure the rabbit is carrying a carrot (status changes from 'r' to 'R').
     - Move the rabbit to an adjacent cell next to a rabbit hole ('O').
     - Use the 'j' key to make the rabbit jump over the hole while carrying a carrot.
     - If the rabbit successfully jumps over a hole and reaches the rabbit hole cell, you win the game!

5. **Exiting the Game**

   - You can quit the game at any time by pressing 'q'.

6. **Have Fun!**

   - Enjoy playing the Rabbit and Carrot Game!

## Author

- Sanjay K J
