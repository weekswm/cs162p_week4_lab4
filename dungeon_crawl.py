#Dungeon Crawl
import random

HERO = ' H '
TRAP = ' T '
TREASURE = ' X '
SPACE_MARKER = ' . '
EASY = 3
MEDIUM = 7
HARD = 11
MAX_SIZE = MEDIUM
DUNGEON = []
game_over = False

'''#Get and Set the difficulty level
def setDifficulty():
    difficulty = input('Set your challenge level:\n E = Easy\n M = Medium\n H = Hard')
    if set_max.upper() == 'H':
        difficulty = HARD
    elif set_max.upper() == 'M':
        difficulty = MEDIUM
    else:
        difficulty = EASY
    return difficulty'''

#Create the Dungeon to size of input
def buildGameBoard(dungeon_floor):
    #iterate through each row on the dungeon floor, adding a SPACE_MAKER for each position
    for row in range(MAX_SIZE):
        list_row = []
        #iterate through each column and at the end of the row start a new line
        for column in range(MAX_SIZE):
            list_row.append(SPACE_MARKER)
            dungeon_floor.append(list_row)
        return dungeon_floor

#Show the dungeon as in its current state
def showDungeon(dungeon_floor):
    print('Move your (H)ero through the dungeon and find the treasure (X) if you dare, but beware of deadly (T)RAPS!\n')
    game_board = ''
    #iterate through each row
    for row in dungeon_floor:
        #show the row
        show_row = ''
        #iterate through each column
        for column in dungeon_floor:
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
def createDungeon(dungeon_floor, num_traps):
    #creates the dungeon of MAX_SIZE by MAX_SIZE
    dungeon_floor = buildGameBoard(dungeon_floor)
    #set traps on the dungeon floor in  random locations
    for each in range(num_traps):
        trap_set = False
        while (not trap_set):
            #pick random location
            row_t = random.randrange(MAX_SIZE)
            column_t = random.randrange(MAX_SIZE)
            #is the square open?
            if dungeon_floor[row_t][column_t] != TRAP:
                dungeon_floor[row_t][column_t] = TRAP
                trap_set = True
    #drop loot in random location
    loot_drop = False
    while (not loot_drop):
        #pick random location
        row_x = random.randrange(MAX_SIZE)
        column_x = random.randrange(MAX_SIZE)
        #is the square open?
        if dungeon_floor[row_x][column_x] != TRAP:
            dungeon_floor[row_x][column_x] = TREASURE
            loot_drop = True
    #set dungeon entry point
    h_spawn = False
    while (not h_spawn):
        #pick random location
        row_h = random.randrange(MAX_SIZE)
        column_h = random.randrange(MAX_SIZE)
        #is the square open?
        if dungeon_floor[row_h][column_h] != TRAP and dungeon_floor[row_h][column_h] != TREASURE:
            dungeon_floor[row_h][column_h] = HERO
            h_spawn = True
    return dungeon_floor

#Set number of traps based on difficulty
def numTraps(MAX_SIZE):
    if MAX_SIZE == EASY:
        num_traps = 1
    elif MAX_SIZE == MEDIUM:
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
        if H in dungeon_floor[row]:
            h_row = row
            h_col = dungeon_floor[row].index(H)
    start_move = (h_row, h_col)
    '''assign movement:
        L, R = col
        U, D = row
        L, D = -
        R, U = +'''
    if move_hero =='L':
        h_col -= 1
    elif move_hero =='R':
        h_col += 1
    elif move_hero =='U':
        h_row += 1
    elif move_hero =='D':
        h_row -= 1
    end_move = (h_row, h_col)
    return start_move, end_move

def check_in_bounds(hero_pos):
    h_row, h_col = hero_pos
    if h_row < 0 or h_row >= MAX_SIZE:
        return True
    elif h_col < 0 or h_col >= MAX_SIZE:
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

def update_dungeon(dungeon_floor, start_move, end_move):
    start_row, start_col = start_move
    end_row, end_col = end_move
    if check_in_bounds(end_move):
        print('Your hero fell to their death. Game over.')
        dungeon_floor[start_row][start_col] = HERO
        game_over = True
    elif check_move(dungeon_floor, end_move, TRAP):
        print('You killed your hero by moving them onto a trap. You murderer! How do you sleep at night?')
        dungeon_floor[end_row][end_col] = HERO
        dungeon_floor[start_row][start_col] = SPACE_MARKER
        game_over = True
    elif check_move(dungeon_floor, end_move, TREASURE):
        print('You found the treasure! You win! Drinks at the tavern are on YOU tonight!')
        dungeon_floor[end_row][end_col] = HERO
        dungeon_floor[start_row][start_col] = SPACE_MARKER
        game_over = True 
    else:
        dungeon_floor[end_row][end_col] = HERO
        dungeon_floor[start_row][start_col] = SPACE_MARKER
        game_over = False
    return game_over, dungeon_floor

#start the dungeon crawl
def play_game(dungeon_floor, game_over = False):
    '''difficulty = input('Set your challenge level:\n E = Easy\n M = Medium\n H = Hard')
    if difficulty.upper() == 'H':
        difficulty = HARD
    elif difficulty.upper() == 'M':
        difficulty = MEDIUM
    else:
        difficulty = EASY
    MAX_SIZE = difficulty'''
    num_traps = numTraps(MAX_SIZE)
    createDungeon(dungeon_floor, num_traps)
    showDungeon(dungeon_floor)
    while (not game_over):
        hero_start_move, hero_end_move = assign_move(dungeon_floor)
        game_over, dungeon_floor = update_dungeon(dungeon_floor, hero_start_move, hero_end_move)
        showDungeon(dungeon_floor)
    play_again = input('Do you dare to brave the dungeon again? Y/y to play again, or any other key to give up and join the rest of the quitters.')
    if play_again.upper() == 'Y':
        new_dungeon = []
        play_game(new_dungeon)
    else:
        print('Good day, to you')
        print('I SAID GOOD DAY!')

play_game(DUNGEON)