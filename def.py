def move_across_hole(rabbit_x,rabbit_y):
    # find_rabbit_hole()
    global adjust_x, adjust_y ,hole_x,hole_y  # Declare adjust_x and adjust_y as global variables
    hole_x,hole_y = find_rabbit_hole(game_map, rabbit_x, rabbit_y)
    
    if not check_adjacent:
        return
    elif rabbit_y == hole_y :
        if rabbit_x == hole_x - 1 :
            adjust_x = hole_x + 1
        elif rabbit_x == hole_x + 1 :
            adjust_x = hole_x - 1
        adjust_y = rabbit_y

    elif rabbit_x == hole_x :
        if rabbit_y == hole_y - 1:
            adjust_y = hole_y + 1
        elif rabbit_y == hole_y + 1 :
            adjust_y =  hole_y - 1
        adjust_x = rabbit_x

    game_map[rabbit_x][rabbit_y] = PATHWAY_STONE
    if status_of_rabbit == 'r':
        game_map[adjust_x][adjust_y] = 'r'
    else:
        game_map[rabbit_x][rabbit_y] = "R"
