#dungeon Crawl
import random

hero = ' H '
trap = ' T '
treasure = ' X '
move_tile = ' . '
easy = 3
medium = 7
hard = 11
#max_size = medium
dungeon = []
game_over = False

#Get and Set the difficulty level
def setDifficulty():
    difficulty = input('Set your challenge level:\n E = easy\n M = medium\n H = hard\n')
    if difficulty.upper() == 'H':
        difficulty = hard
    elif difficulty.upper() == 'M':
        difficulty = medium
    else:
        difficulty = easy
    return difficulty

#Creates a basic dungeon boundaries, populated with the string value ' . '.
def build_game_board(dungeon_floor, max_size):
    # Creates max_size number of rows
    for row in range(max_size):
        list_row = []
        # Creates max_size number of columns
        for column in range(max_size):
            list_row.append(move_tile)
        dungeon_floor.append(list_row)
    return dungeon_floor

#Show the dungeon as in its current state
def show_dungeon(dungeon_floor):
    game_board = ''
    #iterate through each row
    for row in dungeon_floor:
        #show the row
        show_row = ''
        #iterate through each column
        for column in row:
            #add columns to the row
            show_row += column
        #at row end, move down to start new row
        show_row += '\n'
        #add the completed row to the game_board
        game_board += show_row
    #show the completed dungeon
    print(game_board)

"""Now that the base dungeon_floor is set up,
    add traps, treasure, and the player to
    complete the creation of the dungeon"""
def create_dungeon(dungeon_floor, num_traps, max_size):
    #creates the dungeon of max_size by max_size
    dungeon_floor = build_game_board(dungeon_floor, max_size)
    #set traps on the dungeon floor in  random locations
    for each in range(num_traps):
        trap_set = False
        while (not trap_set):
            #pick random location
            row_t = random.randrange(max_size)
            column_t = random.randrange(max_size)
            #is the square open?
            if dungeon_floor[row_t][column_t] != trap:
                dungeon_floor[row_t][column_t] = trap
                trap_set = True
    #drop loot in random location
    loot_drop = False
    while (not loot_drop):
        #pick random location
        row_x = random.randrange(max_size)
        column_x = random.randrange(max_size)
        #is the square open?
        if dungeon_floor[row_x][column_x] != trap:
            dungeon_floor[row_x][column_x] = treasure
            loot_drop = True
    #set dungeon entry point
    h_spawn = False
    while (not h_spawn):
        #pick random location
        row_h = random.randrange(max_size)
        column_h = random.randrange(max_size)
        #is the square open?
        if dungeon_floor[row_h][column_h] != trap and dungeon_floor[row_h][column_h] != treasure:
            dungeon_floor[row_h][column_h] = hero
            h_spawn = True
    return dungeon_floor

#Set number of traps based on difficulty
def define_traps(max_size):
    if max_size == easy:
        num_traps = 1
    elif max_size == medium:
        num_traps = random.randrange(2,4)
    else:
        num_traps = random.randrange(3,7)
    return num_traps

def get_move():
    valid_move = False
    while (not valid_move):
        move_h = input("Choose the direction your hero will move; (L)eft, (R)ight, (U)p, or (D)own?")
        if move_h.upper() == 'L':
            return 'L'
            valid_move = True
        elif move_h.upper() == 'R':
            return 'R'
            valid_move = True
        elif move_h.upper() == 'U':
            return 'U'
            valid_move = True
        elif move_h.upper() == 'D':
            return 'D'
            valid_move = True
        else:
            print('You chose poorly. Did you spend too long in the tavern?')

def assign_move(dungeon_floor):
    move_hero = get_move()
    #locate hero in dungeon
    h_row = -1
    h_col = -1
    for row in range(len(dungeon_floor)):
        if hero in dungeon_floor[row]:
            h_row = row
            h_col = dungeon_floor[row].index(hero)
    start_move = (h_row, h_col)
    '''assign movement:
        L, R = col
        U, D = row
        L, U = -
        R, D = +'''
    if move_hero =='L':
        h_col -= 1
    elif move_hero =='R':
        h_col += 1
    elif move_hero =='U':
        h_row -= 1
    elif move_hero =='D':
        h_row += 1
    end_move = (h_row, h_col)
    return start_move, end_move

def check_in_bounds(hero_pos, max_size):
    h_row, h_col = hero_pos
    if h_row < 0 or h_row >= max_size:
        return True
    elif h_col < 0 or h_col >= max_size:
        return True
    else:
        return False

def check_move(dungeon_floor, hero_pos, trigger):
    #did the hero step in it?
    h_row, h_col = hero_pos
    if dungeon_floor[h_row][h_col] == trigger:
        return True
    else:
        return False

def update_dungeon(dungeon_floor, start_move, end_move, max_size):
    start_row, start_col = start_move
    end_row, end_col = end_move
    if check_in_bounds(end_move, max_size):
        print('Your hero fell to their death. Game over.')
        dungeon_floor[start_row][start_col] = hero
        game_over = True
    elif check_move(dungeon_floor, end_move, trap):
        print('You killed your hero by moving them onto a trap. You murderer! How do you sleep at night?')
        dungeon_floor[end_row][end_col] = hero
        dungeon_floor[start_row][start_col] = move_tile
        game_over = True
    elif check_move(dungeon_floor, end_move, treasure):
        print('You found the treasure! You win! Drinks at the tavern are on YOU tonight!')
        dungeon_floor[end_row][end_col] = hero
        dungeon_floor[start_row][start_col] = move_tile
        game_over = True
    else:
        dungeon_floor[end_row][end_col] = hero
        dungeon_floor[start_row][start_col] = move_tile
        game_over = False
    return game_over, dungeon_floor

#start the dungeon crawl
def play_game(dungeon_floor, game_over = False):
    print('Move your (H)ero through the dungeon and find the treasure (X) if you dare, but beware of deadly (T)RAPS!\n')
    max_size = setDifficulty()
    num_traps = define_traps(max_size)
    create_dungeon(dungeon_floor, num_traps, max_size)
    show_dungeon(dungeon_floor)
    while (not game_over):
        hero_start_move, hero_end_move = assign_move(dungeon_floor)
        game_over, dungeon_floor = update_dungeon(dungeon_floor, hero_start_move, hero_end_move, max_size)
        show_dungeon(dungeon_floor)
    play_again = input('Do you dare to brave the dungeon again? Y/y to play again, or any other key to give up and join the rest of the quitters.')
    if play_again.upper() == 'Y':
        new_dungeon = []
        play_game(new_dungeon)
    else:
        print('Good day, to you')
        print('I SAID GOOD DAY!')

play_game(dungeon)