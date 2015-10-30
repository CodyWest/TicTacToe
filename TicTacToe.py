import random

def test_draw_board(draw_board):
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
    if AI(boarda, "x", "o") != 6:
        print("Error on board a")
    if AI(boardb, "x", "o") != 2:
        print("Error on board b")
    if AI(boardc, "x", "o") != 6:
        print("Error on board c")
    if AI(boardd, "x", "o") != 4:
        print("Error on board d")
    if AI(boarde, "x", "o") != 8:
        print("Error on board e")


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

def check_victory(current_board):
     victory_conditions = [[0,4,8],[2,4,6],[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8]] 
    
        for n in range(len(victory_conditions)): #For each victory condition in victory_conditions
            slots = victory_conditions[n] #Take the victory conditions and put them in a new list
            check = []print
#<<<<<<< HEAD

def get_input(current_board, player_input, turn,):

    print("Turn number ", turn+1)
		if turn % 2 == 0:

			turn = 'X'
		else:
			turn = 'O'
                        

    for i in options(1,9):
        
        player_input=raw_input["Where would you like to go?"]
        
        if player_input != options:
            
            println(player_input,"Is not a valid move buddy. Try again-->")
            
        else if player_input :
            
            print("Nice")
            
            player_input=player_input-1
            
            
            if current_board[player_input]= empty:

                print(player_input, "Is a valid move")

            else:

                print(player_input, " has already been taken. Please select another slot."
        

def update_board(current_board, slot, symbol):
<<<<<<< HEAD
    current_board[slot] = symbol
    return current_board
>>>>>>> origin/master




def TicTacToe():
    current_board = [" "," "," "," "," "," "," "," "," "]
    players = 0
    human = 0
    turn = 1
    while players != 1 and players != 2:
        players = int(raw_input("How many players are there?"))
        if players < 1 or players > 2:
            print("Please pick 1 or 2 players")
    if players == 1:
        difficulty = 0
        while difficulty != 1 and difficulty != 2 and difficulty != 3 and difficulty != 4:
            difficulty = int(raw_input("Pick a difficulty.  1 is easiest, 4 is hardest"))
            if difficulty != 1 and difficulty != 2 and difficulty != 3 and difficulty != 4:
                print("Please pick a difficulty between 1 and 4")
        while human != 1 and human != 2:
            human = int(raw_input("Would you like to go first (1) or second (2)?"))
            if human != 1 and human != 2:
                print("Please pick turn 1 or 2")
    if human == 1:
        player1 = get_input(current_board, int(raw_input("Where would Player 1 like to place their symbol?")) - 1, turn)
        player2 = AI(current_board)
    elif human == 2:
        player1 = AI(current_board)
        player2 = get_input(current_board, int(raw_input("Where would Player 2 like to place their symbol?")) - 1, turn)
    else:
        player1 = get_input(current_board, int(raw_input("Where would Player 1 like to place their symbol?")) - 1, turn)
        player2 = get_input(current_board, int(raw_input("Where would Player 2 like to place their symbol?")) - 1, turn)
    while turn < 10:
        if turn < 3:
            draw_example_board()
        draw_board(current_board)
        if turn%2 == 1:
            update_board(current_board, player1, "X")
        else:
            update_board(current_board, player2, "O")
        check_victory(current_board)
        turn = turn + 1




    print""

