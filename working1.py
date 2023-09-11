
# addded a feature :  unless r picks up carrot r can't move 

# has to jump over holes 

# has replace 'p' instead of j while putting carrot to hole

import os

import random
import sys

status_of_rabbit = 'r'

# Define game constants
RABBIT = 'r'
RABBIT_WITH_CARROT = 'R'
CARROT = 'c'
RABBIT_HOLE = 'O'
PATHWAY_STONE = '-'

appended_list_carrot = []
win = 0
rabbit_hole_list = []

carrot_list = []

# Function to generate a random map
def generate_map(grid, height, num_carrots, num_holes):
    # Create an empty map
    game_map = [[PATHWAY_STONE for _ in range(grid)] for _ in range(height)]

    # Place the rabbit randomly
    rabbit_x, rabbit_y = random.randint(0, grid - 1), random.randint(0, height - 1)
    game_map[rabbit_y][rabbit_x] = RABBIT



    # Place carrots randomly
    for _ in range(num_carrots):
        while True:
            x, y = random.randint(0, grid - 1), random.randint(0, height - 1)
            if game_map[y][x] == PATHWAY_STONE:
                game_map[y][x] = CARROT
                carrot_list.append([y,x])
                break


    # Place rabbit holes randomly
    for _ in range(num_holes):
        while True:
            x, y = random.randint(0, grid - 1), random.randint(0, height - 1)
            if game_map[y][x] == PATHWAY_STONE:
                game_map[y][x] = RABBIT_HOLE
                break

    return game_map

# Function to display the game map
def display_map(game_map):
    os.system('cls' if os.name == 'nt' else 'cls')
    for row in game_map:
        print(' '.join(row))
    print()
    if win == 1:
        print('You Win!')

# Function to find the position of the rabbit
def find_rabbit(game_map):
    for y, row in enumerate(game_map):
        for x, cell in enumerate(row):
            if cell == RABBIT or cell == RABBIT_WITH_CARROT:
                return x, y
    return None, None

# Function to find the position of a rabbit hole adjacent to the rabbit



def find_rabbit_hole(game_map, rabbit_x, rabbit_y):
    adjacent_cells = [(rabbit_x, rabbit_y - 1), (rabbit_x, rabbit_y + 1),
                      (rabbit_x - 1, rabbit_y), (rabbit_x + 1, rabbit_y)]
    for x, y in adjacent_cells:
        if (
            0 <= x < len(game_map[0])
            and 0 <= y < len(game_map)
            and game_map[y][x] == RABBIT_HOLE
        ):
            # print("Adjacent working")
            return x, y
    return None, None



# #********************************************************88

adjust_x, adjust_y = 0, 0  
find_x = 0
find_y = 0


###############################################################


########################################################################

def move_across_hole():
    global adjust_x, adjust_y, find_x, find_y  # Declare adjust_x and adjust_y as global variables
    find_x, find_y = find_rabbit_hole(game_map, rabbit_x, rabbit_y)
    adjust_x, adjust_y = find_rabbit(game_map)
    game_map[adjust_y][adjust_x] = PATHWAY_STONE

    if (
        find_x >= len(game_map[0])
        or find_y >= len(game_map)
        or find_x < 0
        or find_y < 0
    ):
        return
    elif adjust_x == find_x and adjust_y == find_y - 1:
        if find_y + 1 >= len(game_map):
            return
        else:
            adjust_y = find_y + 1
    elif adjust_x == find_x and adjust_y == find_y + 1:
        if find_y - 1 < 0:
            return
        else:
            adjust_y = find_y - 1
    elif adjust_x == find_x - 1 and adjust_y == find_y:
        if find_x + 1 >= len(game_map[0]):
            return
        else:
            adjust_x = find_x + 1
    elif adjust_x == find_x + 1 and adjust_y == find_y:
        if find_x - 1 < 0:
            return
        else:
            adjust_x = find_x - 1
    
    game_map[adjust_y][adjust_x] = "r"



def move_rabbit(game_map, move):
    rabbit_x, rabbit_y = find_rabbit(game_map)
    # print(carrot_list)
    # if [rabbit_y,rabbit_y] not in carrot_list or status_of_rabbit == "R" :
    if move == 'a':
        new_x, new_y = rabbit_x - 1, rabbit_y
    elif move == 'd':
        new_x, new_y = rabbit_x + 1, rabbit_y
    elif move == 'w':
        new_x, new_y = rabbit_x, rabbit_y - 1
    elif move == 's':
        new_x, new_y = rabbit_x, rabbit_y + 1

    else:
        return
    

    if [rabbit_y,rabbit_x] in appended_list_carrot and status_of_rabbit == 'r':
        # print("from 145")
        new_y,new_x = rabbit_y,rabbit_x
        return

    if (
        0 <= new_x < len(game_map[0])
        and 0 <= new_y < len(game_map)
        and game_map[new_y][new_x] != RABBIT_HOLE
        and [rabbit_y, rabbit_x] not in rabbit_hole_list 
    ):
        # if game_map[

        if game_map[new_y][new_x] == CARROT:
            # Rabbit moves to the carrot and picks it up
            game_map[rabbit_y][rabbit_x] = PATHWAY_STONE
            # print("r illi chnage agtide sanju")
            game_map[new_y][new_x] = RABBIT
            appended_list_carrot.append([new_y,new_x])
            
        else:
            # Check if 'R' is adjacent to 'O' (rabbit hole)
            # adjacent_cells = [(rabbit_x, rabbit_y - 1), (rabbit_x, rabbit_y + 1),
            #                   (rabbit_x - 1, rabbit_y), (rabbit_x + 1, rabbit_y)]
            # for x, y in adjacent_cells:
            #     if (
            #         0 <= x < len(game_map[0])
            #         and 0 <= y < len(game_map)
            #         and game_map[y][x] == RABBIT_HOLE
            #     ):
            #         # 'R' reached a rabbit hole, check for win condition
            #         game_map[rabbit_y][rabbit_x] = PATHWAY_STONE

            #         game_map[new_y][new_x] = RABBIT
            #         if check_win(game_map):
            #             display_map(game_map)
            #         return
            
            game_map[rabbit_y][rabbit_x] = PATHWAY_STONE
            if status_of_rabbit == 'r' and game_map[new_x][new_y] !=RABBIT_HOLE :
                # print("still r")
                game_map[new_y][new_x] = RABBIT
            if status_of_rabbit == "R" and game_map[new_x][new_y] !=RABBIT_HOLE :
                 game_map[new_y][new_x] = RABBIT_WITH_CARROT


def check_adjacent(rabbit_y, rabbit_x):
    adjacent_cells = [(rabbit_x, rabbit_y - 1), (rabbit_x, rabbit_y + 1),
                      (rabbit_x - 1, rabbit_y), (rabbit_x + 1, rabbit_y)]
    for x, y in adjacent_cells:
        if (
            0 <= x < len(game_map[0])
            and 0 <= y < len(game_map)
            and game_map[y][x] == RABBIT_HOLE
        ):
            return True
    return False
   

def check_win(game_map):
    for y, row in enumerate(game_map):
        if RABBIT_HOLE in row and CARROT in row:
            return False
    return True

if __name__ == "__main__":
    grid = int(input("Enter map grid: "))
    height = grid 
    num_carrots = int(input("Enter the number of carrots: "))
    num_holes = int(input("Enter the number of rabbit holes: "))
    game_map = generate_map(grid, height, num_carrots, num_holes)

    while True:
        display_map(game_map)
        move = input("Use 'w', 'a', 's', 'd' to move. 'p' to pick up carrots. 'j' to jump over holes. 'q' to quit.\n")

        if move == 'q':
            print("Exiting the game.")
            sys.exit()  # Exit the game

        elif move == 'p' :
            rabbit_x, rabbit_y = find_rabbit(game_map)
            if [rabbit_y,rabbit_x] in carrot_list:
                game_map[rabbit_y][rabbit_x] = 'R'
                status_of_rabbit = "R"
                new_x, new_y = rabbit_x, rabbit_y 
                # print("1st p")
            # move_rabbit(game_map,move,last_place)
            elif status_of_rabbit == "R":
                print("251")
                if check_adjacent(rabbit_y, rabbit_x):
                    # game_map[rabbit_y][rabbit_x] = PATHWAY_STONE
                    win == 1
                    print(255)
                    display_map(game_map)
                    print("Rabbit won ")
                    sys.exit(0)
                  
        elif move == 'j':
            rabbit_x, rabbit_y = find_rabbit(game_map)
            # if [rabbit_y,rabbit_x] in carrot_list and status_of_rabbit == 'r':
            if status_of_rabbit == 'r':
                move_across_hole()
                # print("line 243 declaring new x and y ")
        else:
            move_rabbit(game_map, move)
