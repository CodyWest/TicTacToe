import random

def test_draw_board():
#" " is a blank space
    lista= ["x","x"," "," "," "," "," "," "," "]
    listb= ["x"," "," ","x"," "," "," "," "," "]
    listc= [" "," ","x"," ","x"," ","x"," "," "]
    listd= ["x","o","x","o","x","o","x","o","x"]
    liste= ["x"," ","o","o"," ","x","","o","x"]
    listf= [" "," "," "," "," "," "," "," "," "]
    draw_board(lista)
    draw_board(listb)
    draw_board(listc)
    draw_board(listd)
    draw_board(liste)
    draw_board(listf)

def test_check_victory(check_victory):
    vic1 = ["x","o","x","o","o","x","x","o"," "]
    vic2 = ["x","x","x","o","x","o","x","o","x"]
    vic3 = [" "," "," "," "," "," "," "," "," "]
    vic4 = ["x"," "," ","x"," "," ","x"," "," "]
    vic5 = [" "," "," "," "," "," ","o","o","o"]
    viclist = [vic1, vic2, vic3, vic4, vic5]
    vicanswers = [True, True, False, True, True]
    for n in (0,5):
    	if (check_victory(viclist[n])!=vicanswers[n]):
	   print("Failed on ",viclist[n])
	else:
	   print("Nice")


def test_AI():

    boarda = [" "," "," "," "," "," "," ","x","x"]
    boardb =  ["o","o"," "," "," "," "," "," "," "]
    boardc =  ["o","o"," "," "," "," "," ","x","x"]
    boardd = [" "," "," "," "," "," "," "," "," "]
    boarde = ["x","o"," "," "," "," "," "," "," "]
    if AI(boarda, "x", "o", 4) != 6:
        print("Mistake on board a, diff 4")
    if AI(boardb, "x", "o", 4) != 2:
        print("Mistake on board b, diff 4")
    if AI(boardc, "x", "o", 4) != 6:
        print("Mistake on board c, diff 4")
    if AI(boardd, "x", "o", 4) != 4:
        print("Mistake on board d, diff 4")
    if AI(boarde, "x", "o", 4) != 8:
        print("Mistake on board e, diff 4")
    if AI(boarda, "x", "o", 3) != 6:
        print("Mistake on board a, diff 3")
    if AI(boardb, "x", "o", 3) != 2:
        print("Mistake on board b, diff 3")
    if AI(boardc, "x", "o", 3) != 6:
        print("Mistake on board c, diff 3")
    if AI(boardd, "x", "o", 3) == 4:
        print("Correct on board d, diff 3")
    if AI(boarde, "x", "o", 3) != 8:
        print("Mistake on board e, diff 3")
    if AI(boardd, "x", "o", 3) == 4: #Runs board d a second time, since there's a chance it could come up as correct the first time randomly, so this checks to see if it's a coding error
        print("Correct on board d, diff 3")
    if AI(boarda, "x", "o", 2) != 6:
        print("Mistake on board a, diff 2")
    if AI(boardb, "x", "o", 2) != 2:
        print("Mistake on board b, diff 2")
    if AI(boardc, "x", "o", 2) != 6:
        print("Mistake on board c, diff 2")
    if AI(boardd, "x", "o", 2) == 4:
        print("Correct on board d, diff 2")
    if AI(boarde, "x", "o", 2) == 8:
        print("Correct on board e, diff 2")
    if AI(boardd, "x", "o", 2) == 4:#Runs board d a second time, since there's a chance it could come up as correct the first time randomly, so this checks to see if it's a coding error
        print("Correct on board d, diff 2")
    if AI(boarde, "x", "o", 2) == 8: #Runs board e a second time, since there's a chance it could come up as correct the first time randomly, so this checks to see if it's a coding error
        print("Correct on board e, diff 2")
    if AI(boarda, "x", "o", 1) == 6: 
        print("Correct on board a, diff 1")
    if AI(boardb, "x", "o", 1) == 2:
        print("Correct on board a, diff 1")
    if AI(boardc, "x", "o", 1) == 6:
        print("Correct on board a, diff 1")
    if AI(boardd, "x", "o", 1) == 4:
        print("Correct on board a, diff 1")
    if AI(boarde, "x", "o", 1) == 8:
        print("Correct on board a, diff 1")
    if AI(boarda, "x", "o", 1) == 6: #Runs boards a through e a second time, since there's a chance it could come up as correct the first time randomly, so this checks to see if it's a coding error
        print("Correct on board a, diff 1")
    if AI(boardb, "x", "o", 1) == 2:
        print("Correct on board a, diff 1")
    if AI(boardc, "x", "o", 1) == 6:
        print("Correct on board a, diff 1")
    if AI(boardd, "x", "o", 1) == 4:
        print("Correct on board a, diff 1")
    if AI(boarde, "x", "o", 1) == 8:
        print("Correct on board a, diff 1")


def test_get_input(get_input):
    oldlista= ["x","x"," "," "," "," "," "," "," "]
    oldlistb= ["x"," "," ","x"," "," "," "," "," "]
    oldlistc= [" "," ","x"," ","x","o",""," "," "]
    oldlistd= ["x","o"," ","o"," "," ","x"," ","x"]
    oldliste= ["x"," ","o","o"," "," "," ","o","x"]
    oldlistf= [" "," "," "," "," "," "," "," "," "]
    turn = 0
    input = 7
    
    
#>>>>>>> Stashed changes
def test_update_board(update_board):
    oldlista= ["x","x"," "," "," "," "," "," "," "]
    oldlistb= ["x"," "," ","x"," "," "," "," "," "]
    oldlistc= [" "," ","x"," ","x"," ","x"," "," "]
    oldlistd= ["x","o","x","o","x"," ","x","o","x"]
    oldliste= ["x"," ","o","o"," "," ","","o","x"]
    oldlistf= [" "," "," "," "," "," "," "," "," "]
    old_board_list= [oldlista, oldlistb, oldlistc, oldlistd, oldliste, oldlistf]
    newlista= ["x","x"," "," "," ","x"," "," "," "]
    newlistb= ["x"," "," ","x"," ","x"," "," "," "]
    newlistc= [" "," ","x"," ","x","x","x"," "," "]
    newlistd= ["x","o","x","o","x","x","x","o","x"]
    newliste= ["x"," ","o","o"," ","x","","o","x"]
    newlistf= [" "," "," "," "," ","x"," "," "," "]
    new_board_list= [newlista, newlistb, newlistc, newlistd, newliste, newlistf]
    input_list= ["x", "o", " "]
    slot_list= [1,2,3,4,5,6,7,8,9]
    slot = 3
    current_symbol = "x"
    if update_board(test_board, input, current_symbol)!=["x","o","x","x","x","o"," "," "," "]:
        print("")
     

def AI(current_board, AI_symbol, opponent_symbol, difficulty):
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

                        
    
def draw_example_board():
    example_board_vert_1 = "  1  I  2  I  3  "
    example_board_vert_2 = "  4  I  5  I  6  "
    example_board_vert_3 = "  7  I  8  I  9  "
    example_board_horiz = "_________________"
    
    print(example_board_vert_1)
    print(example_board_horiz)
    print(example_board_vert_2)
    print(example_board_horiz)
    print(example_board_vert_3)
    

def draw_board(current_board):

    board_horiz = "  ''  I  ''  I  ''  "
    board_vert = "_____________________"

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
    
        for n in range(len(victory_conditions)): #For each victory condition in victory_conditions
            slots = victory_conditions[n] #Take the victory conditions and put them in a new list
            check = []print
#<<<<<<< HEAD
=======
    pass #<<<<<<< HEAD
>>>>>>> origin/master

def get_input(current_board, player_input, turn,):

    
    player_input=raw_input["Where would you like to go?"]

    print ("Turn number ",turn+1)
		if int turn % 2 == 0:

    print("Turn number " + str(turn+1))
		if turn % 2 == 0:

			turn = 'X'
		else:
			turn = 'O'

    for player_input in options(1,9):
        

    player_input=raw_input["Where would you like to put your",turn,"?"]
    print "Turn number " + str(turn+1)
    if turn % 2 == 0:
        turn = 'X'
    else:
        turn = 'O'
>>>>>>> Stashed changes
    for i in (1,9):
>>>>>>> origin/master
        if player_input != options:
            
            println(player_input,"Is not a valid move buddy. Try again-->")
            
        else:
            
            print("Nice")
<<<<<<< HEAD
            
            player_input=player_input-1
            
            
            if current_board[player_input]= empty:

                print(player_input, "Is a valid move")

            else:

                print(player_input, " has already been taken. Please select another slot."
        

=======
    #turn++
    
>>>>>>> origin/master
def update_board(current_board, slot, symbol):
    current_board

<<<<<<< Updated upstream



def TicTacToe():
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




    print""
<<<<<<< HEAD

=======
>>>>>>> origin/master
=======
test_draw_board()
>>>>>>> Stashed changes
>>>>>>> origin/master
