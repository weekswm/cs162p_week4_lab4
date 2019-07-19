#Dungeon Crawl
import array
import random

P = ' P '
T = ' T '
X = ' X '
MAX_SIZE = difficulty
EASY = 3
MEDIUM = 7
HARD = 11
ROW = MAX_SIZE
COL = MAX_SIZE
SPACE_MARKER = ' . '
DUNGEON = []

#Get and Set the difficulty level
def setDifficulty():
    difficulty = input('Set your challenge level:\n E = Easy\n M = Medium\n H = Hard')
    if set_max.upper() == 'H':
        difficulty = HARD
    elif set_max.upper() == 'M':
        difficulty = MEDIUM
    else:
        difficulty = EASY
    return difficulty

#Set number of traps based on difficulty
def numTraps(MAX_SIZE)
    if MAX_SIZE == EASY:
        num_traps = 1
    elif MAX_SIZE == MEDIUM:
        num_traps = 3
    else:
        num_traps = 5
    return num_traps

#Create the Dungeon to size of input
def buildGameBoard(dungeon_floor):
    #iterate through each row on the dungeon floor, adding a SPACE_MAKER for each position
    for row in range(MAX_SIZE):
        array_row = []
        #iterate through each column and at the end of the row start a new line
        for column in range(MAX_SIZE):
            array_row.append(SPACE_MARKER)
            dungeon_floor.append(array_row)
        return dungeon_floor

#Show the dungeon as in its current state
def showDungeon(dungeon_floor):
    print('Brave the dungeon and find the treasure, if you dare, but beware of deadly TRAPS!\n')
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
