#TODO: Move import out of main file to a more appropriate area if needed
from random import randint
from time import sleep

#TODO: Allow for boards of different sizes
#TODO: Allow user to import custom boards
#TODO: Abstract the board into a seperate class, migrate board functions to class
#TODO: Add ability to change the characters, colors
#TODO: Migrate drawing to use curses drawing

playBoard = []
#Initializes the game board with a 10x10 grid of ' ', the empty space
for i in range(25):
    playBoard.append([" "] * 25)

#Prints every character in the board with a blank character in between
def PrintBoard(board):
    for row in board:
        print(" ".join(str(col) for col in row))

#TODO: Create the logic for a random starting board
def RandomizeBoard():
    pass

#Creates a pre-populated board for testing purposes
#def TestPopulateBoard():
playBoard = [\
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "], \
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "], \
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "], \
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "], \
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "], \
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", "O", "O", "O", " ", " ", " ", "O", "O", "O", " ", " ", " ", " ", " ", " ", " "], \
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "], \
    [" ", " ", " ", " ", " ", " ", " ", "O", " ", " ", " ", " ", "O", " ", "O", " ", " ", " ", " ", "O", " ", " ", " ", " ", " "], \
    [" ", " ", " ", " ", " ", " ", " ", "O", " ", " ", " ", " ", "O", " ", "O", " ", " ", " ", " ", "O", " ", " ", " ", " ", " "], \
    [" ", " ", " ", " ", " ", " ", " ", "O", " ", " ", " ", " ", "O", " ", "O", " ", " ", " ", " ", "O", " ", " ", " ", " ", " "], \
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", "O", "O", "O", " ", " ", " ", "O", "O", "O", " ", " ", " ", " ", " ", " ", " "], \
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "], \
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", "O", "O", "O", " ", " ", " ", "O", "O", "O", " ", " ", " ", " ", " ", " ", " "], \
    [" ", " ", " ", " ", " ", " ", " ", "O", " ", " ", " ", " ", "O", " ", "O", " ", " ", " ", " ", "O", " ", " ", " ", " ", " "], \
    [" ", " ", " ", " ", " ", " ", " ", "O", " ", " ", " ", " ", "O", " ", "O", " ", " ", " ", " ", "O", " ", " ", " ", " ", " "], \
    [" ", " ", " ", " ", " ", " ", " ", "O", " ", " ", " ", " ", "O", " ", "O", " ", " ", " ", " ", "O", " ", " ", " ", " ", " "], \
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "], \
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", "O", "O", "O", " ", " ", " ", "O", "O", "O", " ", " ", " ", " ", " ", " ", " "], \
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "], \
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "], \
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "], \
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "], \
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "], \
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "], \
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]

#Function to progress the game by one step
def Tick():
    #Initialize a seperate board to protect against destructive changes. Could possibly be optimized
    futurePlayBoard = []
    for i in range(25):
        futurePlayBoard.append([0] * 25)
    
    for row in range(25):
        for col in range(25):
            neighbors = 0
            for x in range(-1,2):
                for y in range(-1,2): 
                    if (row + x >= 0 and row + x <= 24) and (col + y >= 0 and col + y <= 24):
                        if playBoard[row + x][col + y] == "O":
                            neighbors += 1
            #If the current position is equal to "O", the neighbor count would be off by 1. This line prevents that (Could possibly be optimized) 
            if playBoard[row][col] == "O":
                neighbors -= 1
            
            #Populated or Unpopulated check
            #An upopulated cell with 3 neighbors is born
            if playBoard[row][col] == " " and neighbors == 3:
                futurePlayBoard[row][col] = "O"
            #A populated cell with more than 3 neighbors dies
            elif playBoard[row][col] == "O" and neighbors > 3:
                futurePlayBoard[row][col] = " "
            #A populated cell with less than 2 neighbors dies
            elif playBoard[row][col] == "O" and neighbors < 2:
                futurePlayBoard[row][col] = " "
            #If none of the above applies, the cell remains unchanged
            else:
                futurePlayBoard[row][col] = playBoard[row][col]
            
            #Sets futurePlayBoard position to number of neighbors for debug purposes
            """print(str(row),str(col))
            futurePlayBoard[row][col] = neighbors"""
    #Prints futurePlayBoard for testing purposes        
    """PrintBoard(futurePlayBoard)"""
    return futurePlayBoard

#Populates the board
print("Initializing...")
#TestPopulateBoard()
#Main loop
while(True):
    PrintBoard(playBoard)
    print()
    playBoard = list(Tick())
    #usrInput = input("Press ENTER to continue...")
    sleep(.3)