import random

def test_draw_board():
#" " is a blank space
    lista= ["X","X"," "," "," "," "," "," "," "]
    listb= ["X"," "," ","X"," "," "," "," "," "]
    listc= [" "," ","X"," ","X"," ","X"," "," "]
    listd= ["X","O","X","O","X","O","X","O","X"]
    liste= ["X"," ","O","O"," ","X","","O","X"]
    listf= [" "," "," "," "," "," "," "," "," "]
    draw_board(lista)
    draw_board(listb)
    draw_board(listc)
    draw_board(listd)
    draw_board(liste)
    draw_board(listf)

def test_check_victory(check_victory):
    vic1 = ["X","O","X","O","O","X","X","O"," "]
    vic2 = ["X","X","X","O","X","O","X","O","X"]
    vic3 = [" "," "," "," "," "," "," "," "," "]
    vic4 = ["X"," "," ","X"," "," ","X"," "," "]
    vic5 = [" "," "," "," "," "," ","O","O","O"]
    viclist = [vic1, vic2, vic3, vic4, vic5]
    vicanswers = [True, True, False, True, True]
    for n in (0,5):
    	if (check_victory(viclist[n])!=vicanswers[n]):
	   print("Failed on ",viclist[n])
	else:
	   print("Nice")


def test_AI(): #Written by Cody West
    """Tests AI function""" 
    boarda = [" "," "," "," "," "," "," ","X","X"]
    boardb =  ["O","O"," "," "," "," "," "," "," "]
    boardc =  ["O","O"," "," "," "," "," ","X","X"]
    boardd = [" "," "," "," "," "," "," "," "," "]
    boarde = ["X","O"," "," "," "," "," "," "," "]
    if AI(boarda, "X", "O", 4) != 6:
        print("Mistake on board a, diff 4")
    if AI(boardb, "X", "O", 4) != 2:
        print("Mistake on board b, diff 4")
    if AI(boardc, "X", "O", 4) != 6:
        print("Mistake on board c, diff 4")
    if AI(boardd, "X", "O", 4) != 4:
        print("Mistake on board d, diff 4")
    if AI(boarde, "X", "O", 4) != 8:
        print("Mistake on board e, diff 4")
    if AI(boarda, "X", "O", 3) != 6:
        print("Mistake on board a, diff 3")
    if AI(boardb, "X", "O", 3) != 2:
        print("Mistake on board b, diff 3")
    if AI(boardc, "X", "O", 3) != 6:
        print("Mistake on board c, diff 3")
    if AI(boardd, "X", "O", 3) == 4 and AI(boardd, "X", "O", 3) == 4: #Lines like this are meant to check if these functions are getting the right answer consistently, since there's a chance they'll pick the optimal spot randomly
        print("Correct on board d, diff 3")
    if AI(boarde, "X", "O", 3) != 8:
        print("Mistake on board e, diff 3")
    if AI(boarda, "X", "O", 2) != 6:
        print("Mistake on board a, diff 2")
    if AI(boardb, "X", "O", 2) != 2:
        print("Mistake on board b, diff 2")
    if AI(boardc, "X", "O", 2) != 6:
        print("Mistake on board c, diff 2")
    if AI(boardd, "X", "O", 2) == 4 and AI(boardd, "X", "O", 2) == 4:
        print("Correct on board d, diff 2")
    if AI(boarde, "X", "O", 2) == 8 and AI(boarde, "X", "O", 2) == 8:
        print("Correct on board e, diff 2")
    if AI(boarda, "X", "O", 1) == 6 and AI(boarda, "X", "O", 1) == 6: 
        print("Correct on board a, diff 1")
    if AI(boardb, "X", "O", 1) == 2 and AI(boardb, "X", "O", 1) == 2:
        print("Correct on board b, diff 1")
    if AI(boardc, "X", "O", 1) == 6 and AI(boardc, "X", "O", 1) == 6:
        print("Correct on board c, diff 1")
    if AI(boardd, "X", "O", 1) == 4 and AI(boardd, "X", "O", 1) == 4:
        print("Correct on board d, diff 1")
    if AI(boarde, "X", "O", 1) == 8 and AI(boarde, "X", "O", 1) == 8:
        print("Correct on board e, diff 1")


def test_get_input(get_input):#By Josh
    
    current_board= ["X"," ","O","O"," "," "," ","O","X"]
    turnVal = 6
    player_input = 7
    
def test_update_board(): #By Grant
    oldlista= ["X","X"," "," "," "," "," "," "," "]
    oldlistb= ["X"," "," ","X"," "," "," "," "," "]
    oldlistc= [" "," ","X"," ","X"," ","X"," "," "]
    oldlistd= ["X","O","X","O","X"," ","X","O","X"]
    oldliste= ["X"," ","O","O"," "," ","","O","X"]
    oldlistf= [" "," "," "," "," "," "," "," "," "]
    newlista= ["X","X"," "," "," ","X"," "," "," "]
    newlistb= ["X"," "," ","X"," ","X"," "," "," "]
    newlistc= [" "," ","X"," ","X","X","X"," "," "]
    newlistd= ["X","O","X","O","X","X","X","O","X"]
    newliste= ["X"," ","O","O"," ","X","","O","X"]
    newlistf= [" "," "," "," "," ","X"," "," "," "]
    print update_board(oldlistb, 5, "X")
    if update_board(oldlistb, 5, "X") != newlistb:
        print "ye"
    print update_board(oldlistc, 5, "X")
    if update_board(oldlistc, 5, "X") != newlistc:
        print "ye"
    print update_board(oldlistd, 5, "X")
    if update_board(oldlistd, 5, "X") != newlistd:
        print "ye"
    print update_board(oldliste, 5, "X")
    if update_board(oldliste, 5, "X") != newliste:
        print "ye"
    print update_board(oldlistf, 5, "X")
    if update_board(oldlistf, 5, "X") != newlistf:
        print "ye"

def AI(current_board, AI_symbol, opponent_symbol, difficulty): #Written by Cody West
    """Chooses moves for computer based on state of current board and difficulty of AI"""
    victory_conditions = [[0,4,8],[2,4,6],[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8]] #Establishes victory conditions to be checked
    if difficulty >= 2: #If difficulty is at least 2
        for n in range(len(victory_conditions)): #For each victory condition in victory_conditions
            slots = victory_conditions[n] #Take the victory conditions and put them in a new list
            check = [] #Creates empty folder called check
            for i in range(len(slots)): #For each spot in slots
                check.append(current_board[slots[i]]) #Add the corresponding spot from the current board to check
            if check.count(AI_symbol)==2 and check.count(" ")==1: #If there are any rows where the AI has two symbols and there's one empty spot
                return(slots[check.index(" ")]) #Return the empty spot from that row
        for n in range(len(victory_conditions)): #For each victory condition in victory_conditions
            slots = victory_conditions[n] #Take the victory conditions and put them in a new list
            check = [] #Creates empty folder called check
            for i in range(len(slots)): #For each spot in slots
                check.append(current_board[slots[i]]) #Add the corresponding spot from the current board to check
            if check.count(opponent_symbol)==2 and check.count(" ")==1: #If there are any rows where the opponent has two symbols and there's one empty spot
                return(slots[check.index(" ")]) #Return the empty spot from that row
       
    if difficulty >= 3: #If difficulty is at least 3
        for n in range(len(victory_conditions)): #For each victory condition in victory_conditions
            slots = victory_conditions[n] #Take the victory conditions and put them in a new list
            check = [] #Creates empty folder called check
            for i in range(len(slots)): #For each spot in slots
                check.append(current_board[slots[i]]) #Add the corresponding spot from the current board to check
            if check.count(AI_symbol)==1 and check.count(" ")==2: #If there are any rows where the AI has one symbol and there's two empty spots
                if check[0] == " ": #If the first slot from check is empty
                    return(slots[0]) #Return the first slot
                else: 
                    return(slots[2]) #Return the third slot
    if difficulty == 4: #If difficulty is 4
        if current_board[4] == " ": #If the center is empty
            return(4) #Take the center
        elif current_board[0] or current_board[2] or current_board[6] or current_board[8] == " ": #Else, if a corner is open
            corners = 2*random.randint(0,4) #Selects a random corner (or center, which will reject)
            while current_board(corners) != " ": #Until the corner selected is empty
                corners = 2*random.randint(0,4) #Select a new corner or center
            return(corners) #Return empty corner
        else:
            sides = 2*random.randint(0,3)+1 #Selects a side
            while current_board(sides) != " ": #Until the side is empty
                sides = 2*random.randint(0,3)+1 #Selects a new side
            return(sides) #Returns empty side
    if difficulty < 4: #If difficulty is less than 4
        ran = random.randint(0,8) #Picks random spot on board
        while current_board[ran] != " ": #Until the spot is empty
            ran = random.randint(0,8) #Picks a new spot
        return(ran) #Returns empty spot

def create_victory_conditions(size): #Written by Cody West
    """Creates a list of victory conditions based on the size of the board"""
    victory_conditions = []
    for i in range(size):
        horizontal_victory = []
        for n in range(size):
            horizontal_victory.append(size*i+n)
        victory_conditions.append(horizontal_victory)
    for i in range(size):
        vertical_victory = []
        for n in range(size):
            vertical_victory.append(size*n+i)
        victory_conditions.append(vertical_victory)
    diagonal_victory_1 = []
    for i in range(size):
        diagonal_victory_1.append(size*i+i)
    victory_conditions.append(diagonal_victory_1)
    diagonal_victory_2 = []
    for i in range(size):
        diagonal_victory_2.append((i+1)*size-(i+1))
    victory_conditions.append(diagonal_victory_2)
    return(victory_conditions)
        
                        
    
def draw_example_board(): #By Grant
    example_board_vert_1 = "  1  I  2  I  3  "
    example_board_vert_2 = "  4  I  5  I  6  "
    example_board_vert_3 = "  7  I  8  I  9  "
    example_board_horiz = "_________________"
    
    print(example_board_vert_1)
    print(example_board_horiz)
    print(example_board_vert_2)
    print(example_board_horiz)
    print(example_board_vert_3)
    

def draw_board(current_board): #By Grant

    board_vert_1 = "  "+current_board[0]+"  "+"I"+"  "+current_board[1]+"  "+"I"+"  "+current_board[2]+"  " #draws first row of slots and vertcal spacers
    board_vert_2 = "  "+current_board[3]+"  "+"I"+"  "+current_board[4]+"  "+"I"+"  "+current_board[5]+"  " #draws second row of slots and vertical spacers
    board_vert_3 = "  "+current_board[6]+"  "+"I"+"  "+current_board[7]+"  "+"I"+"  "+current_board[8]+"  " #draws third row of slots and verticalspacers
    board_horiz_1 = "_"*len(board_vert_1) #draws first horizontal spacer
    board_horiz_2 = "_"*len(board_vert_2) #draws second horizontal spacer


    print(board_vert_1)
    print(board_horiz_1)
    print(board_vert_2)
    print(board_horiz_2)
    print(board_vert_3)
#print the board
def check_victory(current_board):

    victory_conditions = [[0,4,8],[2,4,6],[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8]] 

    for n in range(victory_conditions): #For each victory condition in victory_conditions
        slots = victory_conditions[n] #Take the victory conditions and put them in a new list
            

def get_input(current_board, player_input, turn,):
                      
    for player_input in options(1,9):

        player_input=raw_input["Where would you like to put your",turn,"?"]
        print ("Turn number ",turn+1)

        if turnVal % 2 == 0:

            turn = 'X'

        else:

            turn = 'O'
        
    for i in (1,9):
        
        if player_input != options:
            println(player_input,"Is not a valid move buddy. Try again-->")
            
        else:
            
            print("Nice")
            
            player_input=player_input-1
            
            if ((current_board[player_input]) == " "):

                print(player_input, "Is a valid move")

            else:

                print(player_input, " has already been taken. Please select another slot.")
    #turn++
    

def update_board(current_board, slot, symbol): #By Grant
    current_board[slot] = symbol
    return current_board


def TicTacToe(): #Written by Cody West
    """Plays Tic Tac Toe"""
    current_board = [" "," "," "," "," "," "," "," "," "] #Empty board
    players = 0 #Number of players
    human = 0 #Indicates whether the human goes first or second (is 0 for two player games)
    turn = 1 #Turn number
    while players != 1 and players != 2: #While a valid number of players has not been chosen
        players = int(raw_input("How many players are there?")) #Asks how many players there are
        if players < 1 or players > 2: #If the choice is not valid
            print("Please pick 1 or 2 players") #Prints error message
    if players == 1: #If 1 player
        difficulty = 0 #Difficulty variable
        while difficulty != 1 and difficulty != 2 and difficulty != 3 and difficulty != 4: #While a valid difficulty has not been chose
            difficulty = int(raw_input("Pick a difficulty.  1 is easiest, 4 is hardest")) #Ask for a difficulty
            if difficulty != 1 and difficulty != 2 and difficulty != 3 and difficulty != 4: #If difficulty choice is not valid
                print("Please pick a difficulty between 1 and 4") #Prints error message
        while human != 1 and human != 2: #While a human turn has not been chosen
            human = int(raw_input("Would you like to go first (1) or second (2)?")) #Ask for human turn
            if human != 1 and human != 2: #If a valid turn is not chosen
                print("Please pick turn 1 or 2") #Print error message
    if human == 1: #If human goes first
        player1 = get_input(current_board, int(raw_input("Where would Player 1 like to place their symbol?")) - 1, turn) #Player 1 is human
        player2 = AI(current_board) #Player 2 is AI
    elif human == 2: #If human goes second
        player1 = AI(current_board) #Player 1 is AI
        player2 = get_input(current_board, int(raw_input("Where would Player 2 like to place their symbol?")) - 1, turn) #Player 2 is human
    else: #If neither
        player1 = get_input(current_board, int(raw_input("Where would Player 1 like to place their symbol?")) - 1, turn) #Player 1 is human
        player2 = get_input(current_board, int(raw_input("Where would Player 2 like to place their symbol?")) - 1, turn) #Player 2 is human
    while turn < 10: #While the number of turns in Tic Tac Toe has not been exceeded
        if turn < 3: #For the first three turns
            draw_example_board() #Draw a board showing the slot numbers
        draw_board(current_board) #Draw current board
        if turn%2 == 1: #If it's an odd numbered turn
            update_board(current_board, player1, "X") #Update board with player 1's selection and X
        else: 
            update_board(current_board, player2, "O") #Update board with player 2's selection and O
        check_victory(current_board) #Check victory
        turn = turn + 1 #Increase turn number


test_draw_board()


test_update_board()
