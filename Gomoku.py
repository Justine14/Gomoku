#The objective of the game is to connect five of your stones in a line to win.
#The lines may be in any direction, that is, either vertically, horizontally, or 
#diagonally. The stones in Gomoku are placed at the intersections of the rows and 
#columns instead of the middle of each cell like a game of Connect 4, for example. The
#board size of Gomoku ranges from 10x10 to 19x19. Many functions are placed within this
#code to separate the turtle drawings, turtle writing, the saving and loading, the
#game states, the winning states, the clicking, and the computer movement. This code 
#is laid out to define all imports first, then all of the turtles, then the window 
#settings, the global variables, and then all of the functions required for the game.



#All import modules.
import turtle
import random

#Creating all turtles required. "welcome" for the board on the turtle
#screen, "jim" for the stones placed by the players.
welcome = turtle.Turtle()
jim = turtle.Turtle()
tess = turtle.Turtle()
jake = turtle.Turtle()
leo = turtle.Turtle()
luke = turtle.Turtle()
blueberry = turtle.Turtle()

blueberry.ht()
luke.ht()
leo.ht()
jake.ht()
tess.ht()
jim.ht()
welcome.ht()

#Creating and setting up the window screen
wn = turtle.Screen()	
wn.bgcolor("AntiqueWhite")

#These global variables are for the the board drawn on the turtle screen.
#Each cell has the length and width of 50 pixels, thus, the length
#and the height are adjusted accordingly to the number of rows and columns 
#chosen for the game.
gridsize = 10
ROWS = gridsize
COLUMNS = ROWS

CELL_SIZE = 50
HALF_CELL_LENGTH = CELL_SIZE / 2

START_X = 0  
START_Y = 0 

LENGTH_OF_BOARD = (COLUMNS * CELL_SIZE)
HEIGHT_OF_BOARD = (ROWS * CELL_SIZE) 

LABLE_LOCATIONX = (START_X)
LABLE_LOCATIONY = (START_Y)

#The margin allows some space between the edges of the board on the turtle
#screen, to the edges of the window screen. The screen height and width are 
#also adjusted accordingly to the number of rows and columns for the board, 
#and may also adjust according to the cell size.
MARGIN = 120
SCREEN_HEIGHT = (2*MARGIN) + (CELL_SIZE * ROWS)
SCREEN_WIDTH= (2*MARGIN) + (CELL_SIZE * COLUMNS)

#The game state of the game, kept in a 2D list.
GRID = [['-'] * ROWS for x in range(ROWS)]

#Initializes variable to 0, where 'COLOR' is a choice for the player to choose
#whether they would like to play with a white or a black stone. 0 is assigned
#to white, and 1 is assigned to black.
COLOR = 0
TURN = 0

#Intializes a truth value for the function isGameDone.
isGameDone = False
#Initializes the file name for the saving and loading files
filename = "gomokuSaved.txt"

#This function adds ASCII art
def introduction():
	print("""
 __    __     _                                                
/ / /\ \ \___| | ___ ___  _ __ ___   ___                  
\ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \                    
 \  /\  /  __/ | (_| (_) | | | | | |  __/                        
  \/  \/ \___|_|\___\___/|_| |_| |_|\___|                                
 _         
| |                                    
| |_  ___                                        
| __|/ _ \                                     
| |_| (_) |                                 
 \__|\___/  
                                                 
   _____                           _            _  _ 
  / ____|                         | |          | || |
 | |  __   ___   _ __ ___    ___  | | __ _   _ | || |
 | | |_ | / _ \ | '_ ` _ \  / _ \ | |/ /| | | || || |
 | |__| || (_) || | | | | || (_) ||   < | |_| ||_||_|
  \_____| \___/ |_| |_| |_| \___/ |_|\_\ \__,_|(_)(_)
""")


#This function uses the turtle blueberry to draw 10 boxes for players to 
#be able to choose what grid size they would like to play on.
#No parameters are passed, nothing is returned
def optionsForBoardSize():
	blueberry.up()
	blueberry.goto(-250, 90)
	blueberry.down()
	blueberry.speed(0)
	for tenOptions in range(0, 10):
		for eachSquare in range(4):
			blueberry.forward(50)
			blueberry.right(90)
		blueberry.forward(50)
	blueberry.up()

#This function uses the turtle blueberry to draw the boxes for the player
#to choose whether they would like to play with a white or a black stone
#No parameters are passed and nothing is returned
def optionsForColour():
	blueberry.goto(-150, -20)
	blueberry.down()
	for drawWhiteOrBlackButton in range(2):
		for drawSquare in range(2):
			blueberry.forward(100)
			blueberry.right(90)
			blueberry.forward(50)
			blueberry.right(90)
		blueberry.up()
		blueberry.forward(200)
		blueberry.down()
	blueberry.up()

#Uses the turtle blueberry to draw the start button. This begins the drawing 
#of the board and implements the rest of the game when clicked.
#There are no parameters and nothing is returned
def startButton():
	blueberry.goto(-100, -100)
	blueberry.down()
	for drawiSquareTwo in range(4):
		blueberry.forward(200)
		blueberry.right(90)
		blueberry.forward(80)
		blueberry.right(90)
	blueberry.up()


#The turtle blueberry writes words on the introduction screen
#No parameters and nothing returned
def writingForIntro():
	blueberry.color("DodgerBlue")
	blueberry.pensize(5)
	blueberry.speed(20)
	blueberry.up()
	blueberry.goto(0, 210)
	blueberry.down()
	blueberry.write("Gomoku!", align="center", font=("Arial",50, "normal")) 

	blueberry.up()
	blueberry.goto(0, 175)
	blueberry.down()
	blueberry.write("Welcome to this amazing game called Gomoku!",align="center", font=("Arial",15, "normal")) 

	blueberry.up()
	blueberry.goto(-255, 100)
	blueberry.write("How many rows and columns would you like to play on?", font=("Bauhaus 93", 16, "normal"))
	startWriting = -230
	for integers in range(10, 20, 1):
		blueberry.goto(startWriting, 60)
		blueberry.write(integers)
		startWriting = startWriting + 50

	blueberry.up()
	blueberry.goto(-248, -10)
	blueberry.write("Please choose the colour you would like to play with", font=("Bauhaus 93", 16, "normal"))

	blueberry.up()
	blueberry.goto(-115, -50)
	blueberry.write("White")

	blueberry.goto(88, -50)
	blueberry.write("Black")

	blueberry.up()
	blueberry.goto(-25, -150)
	blueberry.write("Start!", font=("Bauhaus 93", 16, "normal"))

	blueberry.up()
	blueberry.goto(-300, -230)
	blueberry.write("This is a 2 player game where you use either a black or a white stone. The objective is to", font=("Candara", 12, "normal"))
	blueberry.goto(-320, -260)
	blueberry.write(" connect 5 of your stones in a line to win. Connecting 6 or more in a line will not count as a win.", font=("Candara", 12, "normal"))
	blueberry.goto(-320, -290)
	blueberry.write("To pick a correct value, please click between the board boundaries and at the row and column ", font=("Candara", 12, "normal"))
	blueberry.goto(-25, -320)
	blueberry.write("intersections.", font=("Candara", 12, "normal"))
	blueberry.up()
	blueberry.ht()

#At the beginning of the game, the options for the board size, the colour, 
#and the start button are handled in this function. It checks the range of all 
#buttons clicked in the main menu screen.
#Parameters:
			#x: class float, this is the x pixel coordinates
			#y: class float, this is the y pixel coordinates
#Returns: gridsize, class int, for the numbers of rows and columns, or in other
#words, the size of the board
def startOfGameClicks(x,y):
	global COLOR	
	global gridsize
	theStart = -250
	blueberry.shape('turtle')
	blueberry.color('Light Salmon')
	#This loop is to handle board size
	#The input for choosing board size by click is used to 
	#update all global variables  
	for handleGrid in range(0, 11):
		if ( (x >= (theStart +(handleGrid*50))) and (x <= theStart + (50*(handleGrid+1))) and ((y <= 90) and (y >= 40)) ):
			gridsize = (handleGrid+10)
			blueberry.up()	
			blueberry.goto(x,y)
			blueberry.stamp()
			moveIntroStamp(x,y)
			UpdateGlobalVariable()
			return gridsize

	#To handle if player chose white
	if ( (x >= -150) and (x <= -50) and (y <= -20) and (y >= -70) ):
		COLOR = 0
		blueberry.up()
		blueberry.goto(x,y)
		blueberry.stamp()
		moveIntroStamp(x,y)
	#To handle if player chose black
	if ( (x >= 50) and (x <= 150) and (y <= -20) and (y >= -70) ):
		COLOR = 1
		blueberry.up()
		blueberry.goto(x,y)
		blueberry.stamp()
		moveIntroStamp(x,y)

	#Handle the startButton in the required range.
	#If clicked in this range then call function officialGame()
	if ( (x >= -100) and (x <= 100) and (y <= -100) and (y >= -180) ):
		blueberry.ht()
		officialGame()

#This function clears the previous stamp from the turtle blueberry if the 
#player decides to choose another option
#Parameters:
			#x: class float, this is the x pixel coordinates
			#y: class float, this is the y pixel coordinates
#Returns nothing 
def moveIntroStamp(x,y):
	blueberry.clearstamps()
	blueberry.up()
	blueberry.goto(x,y)
	blueberry.stamp()

#This function will take all values from the introduction screen and
#then updates all global variables to suit the players game requirements
def UpdateGlobalVariable():
	global ROWS
	global gameState
	global gridsize
	global COLUMNS
	global LENGTH_OF_BOARD
	global HEIGHT_OF_BOARD
	global SCREEN_HEIGHT
	global SCREEN_WIDTH
	global GRID

	ROWS = gridsize
	COLUMNS = ROWS
	
	LENGTH_OF_BOARD = (COLUMNS * CELL_SIZE)
	HEIGHT_OF_BOARD = (ROWS * CELL_SIZE) 

	SCREEN_HEIGHT = (2*MARGIN) + (CELL_SIZE * ROWS)
	SCREEN_WIDTH= (2*MARGIN) + (CELL_SIZE * COLUMNS)
		
	GRID = [['-'] * ROWS for x in range(ROWS)]

	gameState = GRID

#This function draws the game board on the turtle screen. 
#It takes in no parameters, but includes two for loops. The 
#outer for loop will draw the columns, whereas the inner for loops 
#will draw the rows. 
#Nothing is returned.
def GameBoard():
	RowNum = START_Y
	for theCol in range(COLUMNS - 1):
		ColumnNum = START_X	
		for theRow in range(ROWS - 1):
			draw_square(ColumnNum, RowNum)
			ColumnNum = ColumnNum + CELL_SIZE
		RowNum = RowNum + CELL_SIZE

#The turtle 'welcome' draws the size of each cell for the number of rows and
#columns for the function GameBoard(). 
#This function takes two parameters:
		#START_X, START_Y. Values located at 0,0 as pixels on the turtle screen. 
		#These parameters are class int. 
#Nothing is returned
def draw_square(START_X, START_Y):
	turtle.tracer(0)
	welcome.up()
	welcome.speed(10)
	welcome.goto(START_X, START_Y)
	welcome.down()
	for eachCell in range(4):
		welcome.forward(CELL_SIZE)
		welcome.left(90)
	welcome.ht()
	turtle.update()
	turtle.tracer(0)				

#Writes the row numbers and column numbers on the turtle screen. No parameters
#are used. The row and column numbers range from 0 to the value the user clicks
#on the main menu.
#There are no parameters
#Returns nothing
def labels():
	global LABLE_LOCATIONY
	global LABLE_LOCATIONX
	#Turtle 'welcome' writes y-values for all values starting at 0 and
	#incrementing by 1 according to the number of rows.
	for yValueLabels in range(0, ROWS):
		welcome.up()
		welcome.goto(LABLE_LOCATIONX - 5, LABLE_LOCATIONY - 50)
		welcome.write(str(yValueLabels), font=("Arial",15,"normal"))
		LABLE_LOCATIONX = LABLE_LOCATIONX + CELL_SIZE
		welcome.ht()
	
	LABLE_LOCATIONX = 0		#Resets the location of x to 0
	#Turtle 'welcome' writes all x-values starting at 0 and
	#incrementing by 1 according to the number of rows.
	for xValueLabels in range(0, COLUMNS):
		welcome.up()
		welcome.goto(LABLE_LOCATIONX - 35, LABLE_LOCATIONY - 10)
		welcome.write(str(xValueLabels), font=("Arial",15,"normal"))
		LABLE_LOCATIONY = LABLE_LOCATIONY + CELL_SIZE
		welcome.ht()

#This function uses turtles to draw the save button, the load button, and the 
#turn on the game screen. The turtle jim shows in the turn slot which player
#has the turn. 
#There are no parameters
#Nothing returned
def SaveLoadTurnDrawing():
	global COLOR

	jake.speed(10)
	jake.up()
	jake.goto(-165, 100)
	jake.down()
	for drawing in range(2):
		jake.pencolor("red")
		jake.forward(100)
		jake.right(90)
		jake.forward(50)
		jake.right(90)
	jake.up()
	jake.goto(-135, 65)
	jake.write("Save")
	jake.ht()
		
	leo.up()
	leo.speed(10)
	leo.goto(-165, 35)
	leo.down()

	for drawing in range(2):
		leo.pencolor("black")
		leo.forward(100)
		leo.right(90)
		leo.forward(50)
		leo.right(90)
	leo.up()
	leo.goto(-135, 0)
	leo.write("Load")
	leo.ht()

	tess.color("OrangeRed")
	tess.shape("circle")
	tess.speed(10)
	tess.up()
	tess.goto(-165, 300)
	tess.down()
	for theDrawing in range(2):
		tess.forward(115)
		tess.left(90)
		tess.forward(50)
		tess.left(90)
	tess.color("black")
	tess.up()
	tess.goto(-155, 310)
	tess.pensize(5)
	tess.write("Turn:", align = "left", font = ("Arial",15, "normal"))
	tess.ht()

	if COLOR == 0:
		jim.color("white")
	else:
		jim.color("black")
	jim.up()
	jim.shape("circle")
	jim.goto(-75, 325)
	jim.stamp()
	jim.ht()


	luke.speed(10)
	luke.up()
	luke.goto(-150, -85)
	luke.down()
	luke.pencolor("black")
	luke.pensize(5)
	for drawing in range(2):
		luke.forward(700)
		luke.right(90)
		luke.forward(175)
		luke.right(90)
	luke.ht()

#On the game screen, this function allows the turtle luke to write all statements
#within the space provided at the bottom of the game board.
#There are no parameters
#Nothing returned
def screenWriting(writes_this):
	luke.up()
	luke.goto(-115, -175)
	luke.write(writes_this, align = "left", font = ("Arial",15, "normal"))

#This function saves the file into a text document called gomokuSaved.txt. While
#the file is open, the lines on the current grid will be written on the save file.
#The lines are written line for line, and each line gets joined for the number
#of lines in the grid. The file closes once it is done. The file gomokuSaved.txt is 
#global, by the variable filename
#No parameters are used
#Returns nothing 
def saveFile():
	with open(filename, 'w') as f:
		f.writelines(str(ROWS) + '\n')
		f.writelines(''.join(str(j) for j in i) + '\n' for i in GRID)
	luke.undo()
	screenWriting("Save Completed!")
	f.close()	

#This function loads the file from the text document gomokuSaved.txt. Once this
#file is opened, the file will be read, and the grid, game state, and game will
#be updated. This function uses the try and except method. If the file is found,
#all statements within the try are executed. If the file is not found, it will 
#except an IOError, and tell the individual that gomokuSaved.txt could not be
#opened.
#No parameters are passed
#Nothing is returned.
def loadFile():	
	global GRID
	global ROWS
	global gameState
	i = 0
	j = 0
	try:
		with open(filename) as f:
			luke.undo()
			screenWriting("The file is now loaded.")
			newSize = f.readline()
			ROWS = int(newSize)
			COLUMNS = ROWS
			GRID = [['-'] * ROWS for x in range(ROWS)]
			while True:
				character = f.readline().rstrip('\n')
				print(character)
				if not character:
					break
				while j < ROWS:
					GRID[i][j] = character[j]
					j = j + 1
				j = 0
				i = i + 1
				if i >= ROWS:
					gameState = GRID
					break
			f.close()
	except IOError:
		luke.undo()
		screenWriting("gomokuSaved.txt could not be opened")
	twoDlistGamestate()

#This function takes the clicks at the pixels and handles the save or load
#buttons. If the user clicks within the save button boundaries, the function
#saveFile will be called. If the user clicks within the load button boundaries,
#the function loadFile will be called. If the load file function is called, 
#all current moves on the board will be removed and the previously saved file 
#will be loaded. The gameState will also be updated.
#Parameters:
		#x: class float. This is the x coordinate pixel.
		#y:	class float. This is the y coordinate pixel.
#Returns:
		#True: if user clicks within the save button boundaries or within the load
		#button boundaries, the function will return True.
		#False: if both buttons do not return true, return False.
def handleSaveOrLoadButton(x,y):
	if ( ((x >= -165) and (x <= -65)) and ((y <= 100) and (y >= 50)) ) : 
		wn.onclick(saveFile(), btn=1, add=None)
		return True
	elif ( ((x >= -165) and (x <= -65)) and ((y <= 35) and (y >= -15)) ): 
		wn.onclick(loadFile(), btn=1, add=None)
		#This will undo the moves on the current file if stones were placed but 
		#the previously saved game needs to be loaded
		for undoStones in range(ROWS * COLUMNS):
			jim.undo()
		for allRows in range(ROWS):
			for allCol in range(COLUMNS):
				if GRID[allRows][allCol] == 'B':
					jim.color('black')
					jim.up()
					jim.goto((allCol * 50),(allRows * 50))
					jim.stamp()
				elif GRID[allRows][allCol] == 'W':
					jim.color('white')
					jim.up()
					jim.goto((allCol * 50),(allRows * 50))
					jim.stamp()
		return True
	return False


#This function uses the random module to determine whether the computer or the
#player will go first. 
#No parameters are required.
#Returns none
def whichPlayerGoesFirst():
	global TURN
	TURN = random.randint(0,1)
	if TURN == 0:
		screenWriting("Computer will go first")
	else:
		screenWriting("Player will go first")
	return TURN

#This function is for the computer to use the randomly generated integer and
#make it into a real, valid move on the board. This function will check if the
#computer move is valid, will draw the stone on the board, and will update the 
#2D list, with the right color of stone the computer must play with. This is a 
#recursive if the random generated move isn't valid.
#No parameters are passed
#Nothing is returned
def AI_movement():
	(col, row)= random_move_generate()
	if not check_board_full():
		return
	if isMoveValid(row, col):
		drawItemOnBoard(col, row)
		updatetwoDlistGamestate(row, col)
		changeColor()
	else:
		AI_movement()

#This function will generate a random move for the computer to make. A random
#integer for the x and y pixel values will be chosen for the computer. Those 
#pixel values are then converted to column and row values to be successfully 
#placed on the board.
#No parameters are required.
#Returns: 
		#col: class int. This is the column number on the board.
		#row: class int. This is the row number on the board.
def random_move_generate():
	global ROWS
	global COLUMNS
	row = random.randint(0, (ROWS - 1))
	col = random.randint(0, (COLUMNS - 1))
	return(col, row)

#Checks whether the spot is taken or if it's empty.
#Parameters:
		#col: class int. The x-values on the board.f
		#row: class int. The y-values on the board.
#Returns: gameState, truth value of index, class list.
def isMoveValid(row, col):
	global gameState
	return gameState[row][col] == '-'

#This function will check if the board is full for the AI movements by looking
#at the game state. If the board is full, the AI will not make a move.
#No parameters required
#Returns:
		#True: if the board is not full and empty spaces are still found in the gameState
		#False: if there are no empty spaces located on the gameState.
def check_board_full():
	spot = 0
	for eachRow in range(ROWS):
		for eachCol in range(COLUMNS):
			if gameState[eachRow][eachCol] == '-':
				return True
			else:
				return False

#This function switches the color after each move
#No parameters
#Returns:
	#COLOR: a global variable, class int.
def changeColor():
	global COLOR
	if (COLOR == 0):
		COLOR = 1
	else:
		COLOR = 0
	return COLOR

#This function creates the 2D list and incorporates the game state.
#There are no parameters.
#Returns: 
		#GRID, class list.
def twoDlistGamestate():
	for rowNum in range (ROWS):
		print(GRID[rowNum][0:])
	return GRID

#Assigns the variable gameState to the global variable GRID.
gameState = GRID

#This function updates the list whenever a white or black stone is placed on
#the board. 'W' represents write, 'B' represents black.
#Parameters: 
		#col: class int, converted into integers from 
		#row: class int
#Returns: the gameState, class list. 
def updatetwoDlistGamestate(row, col):
	global COLOR
	global gameState
	if (COLOR == 0):
		gameState[row][col] = 'W'
	else:
		gameState[row][col] = 'B'
	return gameState

		
#Checks the winning states hoizontally, vertically, or diagonally.
#Parameters:
		#col: class int. This is the x-values on the board.
		#row: class int. This is the y-values on the board.
#Returns: 
		#isWinningVertical(row,col): if counter in this function is equal to 5 and
		#returns True, than this function will be returned.
		#isWinningHorizontal(row,col): if counter in this function is equal to 5
		#and returns True, this function will be returned.
		#isWinningdiagonal(row,col): if counter is equal to 5 in this function, than
		#this function will be returned.
		#The logical operator 'or' is used to check if at least one of the functions
		#return True
def isWinning(row, col):
	return isWinningVertical(row, col) or isWinningHorizontal(row, col) or isWinningDiagonal(row, col)

#This function iterates through the gameState to determine whether there are 
#5 consecutive same colored stones horizontally, but no more than 5.
#Parameters:
		#col: class int. This is the x-values on the board.
		#row: class int. This is the y-values on the board.
#Returns: 
		#True if winning state meets all conditions, if counter is equal to 5.
		#False otherwise.
def isWinningHorizontal(row, col): 
	global gameState
	global COLOR

	counter = 0
	
	if COLOR == 0:
		str_variable = 'W'
	else:
		str_variable = 'B'

	#This for loop checks the list in both directions, reading from left to
	#right and right to left.
	for direction in [1, -1]:
		i = 0
		curPos = col
		while ( 0 <= curPos < COLUMNS and  gameState[row][curPos] == str_variable):
			counter += 1	
			i += 1				
			curPos = col + i*direction
	counter -= 1
	
	if counter == 5: 
		return True 
	else:	
		return False  

#This function iterates through the gameState to determine whether there are 
#5 consecutive same colored stones vertically, but no more than 5.
#Parameters:
		#col: class int. This is the x-values on the board.
		#row: class int. This is the y-values on the board.
#Returns: 
		#True if counter is equal to 5.
		#False otherwise
def isWinningVertical(row, col):
	global gameState
	global COLOR
    
	counter = 0

	if COLOR == 0:
		str_variable = 'W'
	else:
		str_variable = 'B'
	for direction in [1, -1]:
		i = 0
		curPos = row
		while ( 0 <= curPos < ROWS and  gameState[curPos][col] == str_variable):
			counter += 1	
			i += 1				
			curPos = row + i*direction
	counter -= 1
	
	if counter == 5: 
		return True 
	else:	
		return False  

#This function iterates through the gameState to determine whether there are 
#5 consecutive same colored stones diagonally in either direction, but no 
#more than 5.
#Parameters: 
		#col: class int. This is the x-values on the board.
		#row: class int. This is the y-values on the board.
#Returns: 
		#True if counter is equal to 5.
		#False otherwise
def isWinningDiagonal(row, col):
	global gameState
	global COLOR
	global ROWS
	global COLUMNS
	
	counter1 = 0
	counter2 = 0

	if COLOR == 0:
		str_variable = 'W'
	else:
		str_variable = 'B'	

	curRow = row
	curCol = col

	#checks diagonally up and left
	while( 0<= curRow < ROWS and 0 <= curCol < COLUMNS and gameState[curRow][curCol] == str_variable):
		curRow += 1
		curCol -= 1
	
	#checks diagonally down and right
	curRow2 = row
	curCol2 = col
	while( 0<= curRow2 < ROWS and 0 <= curCol2 < COLUMNS and gameState[curRow2][curCol2] == str_variable):
		curRow2 -= 1
		curCol2 += 1

	#checks diagonally up and right
	curRow3 = row
	curCol3 = col
	while( 0<= curRow3 < ROWS and 0 <= curCol3 < COLUMNS and gameState[curRow3][curCol3] == str_variable):
		curRow3 += 1
		curCol3 += 1
			
	#checks diagonally down and left
	curRow4 = row
	curCol4 = col
	while( 0<= curRow4 < ROWS and 0 <= curCol4 < COLUMNS and gameState[curRow4][curCol4] == str_variable):
		curRow4 -= 1
		curCol4 -= 1

	counter1 = curRow - curRow2 - 1
	counter2 = curRow3 - curRow4 - 1

	if (counter1 == 5) or( counter2 == 5): 
		return True 
	else:
		return False  


#Checks and prints which player wins if they have met all conditions.
#No parameters
#Returns:
		#isGameDone: the function isGameDone is originally set to False. Once
		#the function isWinning is true, this is returned and the game is over
def gameOver():
	global isGameDone
	isGameDone = True
	if COLOR == 0:
		luke.undo()
		screenWriting("White, wins!")
	else:
		luke.undo()
		screenWriting("Black, wins!")
	return isGameDone

#This function converts the pixel coordinates into coordinates shown on the 
#game board.
#Parameters: x,y. Class float. Taken from function clicked(x,y)
		#x: uses the x values of pixels and makes them into board columns
		#y: uses y-values of pixels and makes them into board rows
#Returns: Nothing
def screenCoordToBoardCoord(x, y):
	#This is the range of the board, print invalid if click outside of the range
	#There is a 15 pixel margin of error
	if (((x >= (START_X - 15)) and (x <= (START_X + 15 +(LENGTH_OF_BOARD))) and (y <= (START_Y + 15) + (HEIGHT_OF_BOARD) and (y >= (START_Y - 15))))):   
		col = (int((x + HALF_CELL_LENGTH)/ CELL_SIZE))
		row = (int((y + HALF_CELL_LENGTH)/  CELL_SIZE))
		return(col, row)
	else:
		luke.undo()
		screenWriting("Invalid!")
		return 

#Uses the turtle module to stamp a stone wherever the user clicks or the 
#computer moves.
#Parameters: col, row. Class int
			#col: from x value pixels, is the x values on the board
			#row: from y value pixels, is the y values on the board
def drawItemOnBoard(col, row):
	global COLOR
	global isGameDone
	if not isGameDone:
		if COLOR == 0:
			jim.color("white")
		else:
			jim.color("black")
		jim.shape("circle")
		jim.shapesize(1)
		jim.speed(10)
		jim.up()
		jim.goto((col * CELL_SIZE), (row * CELL_SIZE))
		jim.stamp()
		jim.ht()
	else:
		return  

#Will take user clicks and change pixels to board coordinates, check if every
#move made is valid, if so, draws the item on the board, then updates the 2D list.
#Parameters: 
		#x: class float
		#y: class float
#Returns: Nothing / null
def clicked(x,y):
	global turn	
	global gameState
	global isGameDone
	global COLOR

	if (isGameDone):
		return
	
	handler = handleSaveOrLoadButton(x,y)
	#The function handleSaveOrLoadButton(x,y) must go outside of the boundaries of 
	#the board. Thus, to allow clicking in the save or load buttons, if the range
	#is not within the save or load buttons, than the user may click anywhere
	#else within the board.
	if not handler:
		results = screenCoordToBoardCoord(x,y)
		if results == None:
			return
		(col, row) = results

		if not isMoveValid(row, col):
			luke.undo()
			screenWriting("Someone has moved there already pick again!")
			return

		drawItemOnBoard(col, row)
		updatetwoDlistGamestate(row, col)

		for line in reversed(gameState):
			print(line)

		if isWinning(row,col):
			gameOver()
			return

		changeColor() 
		AI_movement()
	else:
		wn.onscreenclick(clicked, btn=1, add=None)
	

#This function calls to other functions to set up the board and the 2D list. 
#These functions will draw the titles, labels, make the screensize, and complete
#the 2D list.
#No parameters are passed
#Nothing is returned
def setup():
	global ROWS
	global COLUMNS
	ROWS = gridsize
	COLUMNS = ROWS
	wn.setworldcoordinates(-250, -250, 700, 750)				#Setting World Coordinates
	wn.setup(SCREEN_HEIGHT, SCREEN_WIDTH, startx=0, starty=0)	#Adjusting Screen Setup
	#GameBoard Setup:
	labels()
	SaveLoadTurnDrawing()
	GameBoard()
	blueberry.ht()
	luke.ht()
	leo.ht()
	jake.ht()
	tess.ht()
	jim.ht()
	welcome.ht()
	
#This function is called when the user clicks the start button on the main menu.
def officialGame():
	global COLOR
	introduction()
	setup()
	whichPlayerGoesFirst()
	
	if TURN == 0:
		if COLOR == 0:
			COLOR = 1
		else:
			COLOR = 0
		AI_movement()

	wn.onscreenclick(clicked, btn=1, add=None)
	wn.mainloop()


def main():
	global COLOR

	writingForIntro()
	optionsForBoardSize()
	optionsForColour()
	startButton()
	wn.onscreenclick(startOfGameClicks, btn=1, add=None)

	wn.mainloop()


main()

#Group 76 
#Members: Ali Akbari, Justine Bui
#Game: Gomoku 
# DISCLAIMER: There is only one mode called easy mode where the player always wins.
# Turn button icon color appears to not show change because the computer makes their turn fast.
