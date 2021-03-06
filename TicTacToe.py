import random

def test_draw_board(): #By Grant
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


def test_get_input():#By Josh
    
    current_board= ["X"," ","O","O"," "," "," ","X","X"]

    print type(get_input(current_board, 6,7))==int
    print type(get_input(current_board, "utjdf", 7))==int
    print type(get_input(current_board, 1, 7))==int
    new_current_board= ["X"," ","O","O"," "," ","O","X","X"]
    

    if current_board == new_current_board:
        print "Success!"
    else:
        print "Error"
    
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
    if update_board(oldlistb, 5, "X") == newlistb:
        print "ye"
    print update_board(oldlistc, 5, "X")
    if update_board(oldlistc, 5, "X") == newlistc:
        print "ye"
    print update_board(oldlistd, 5, "X")
    if update_board(oldlistd, 5, "X") == newlistd:
        print "ye"
    print update_board(oldliste, 5, "X")
    if update_board(oldliste, 5, "X") == newliste:
        print "ye"
    print update_board(oldlistf, 5, "X")
    if update_board(oldlistf, 5, "X") == newlistf:
        print "ye"
 
def AI(current_board, AI_symbol, opponent_symbol, difficulty): #Written by Cody West
    """Chooses moves for computer based on state of current board and difficulty of AI"""
    victory_conditions = [[0,4,8],[2,4,6],[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8]] #Establishes victory conditions to be checked
    if difficulty >= 2: #If difficulty is at least 2
        ## Cody -- you could just write:
        ## for slots in victory_conditions
        for n in range(len(victory_conditions)): #For each victory condition in victory_conditions ## Oops
            slots = victory_conditions[n] #Take the victory conditions and put them in a new list ## Oops 
            check = [] #Creates empty folder called check
            for i in range(len(slots)): #For each spot in slots
                check.append(current_board[slots[i]]) #Add the corresponding spot from the current board to check
            ## This you can do even more efficiently using a beautiful syntax called
            ## "list comprehension" which entered python some years ago -- watch
            ## me do it in one line:
            ## check = [current_board[s] for s in slots]
            if check.count(AI_symbol)==2 and check.count(" ")==1: #If there are any rows where the AI has two symbols and there's one empty spot
                return(slots[check.index(" ")]) #Return the empty spot from that row
        ## Oops -- you repeat the code again here for no reason
        for n in range(len(victory_conditions)): #For each victory condition in victory_conditions
            slots = victory_conditions[n] #Take the victory conditions and put them in a new list
            check = [] #Creates empty folder called check
            for i in range(len(slots)): #For each spot in slots
                check.append(current_board[slots[i]]) #Add the corresponding spot from the current board to check
            if check.count(opponent_symbol)==2 and check.count(" ")==1: #If there are any rows where the opponent has two symbols and there's one empty spot
                return(slots[check.index(" ")]) #Return the empty spot from that row
    if difficulty >= 3: #If difficulty is at least 3
        ## It looks like you're doing an identical loop here -- I
        ## wonder why you don't move the if statement inside the loop
        ## -- I believe that would significantly shorten your code
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
            while current_board[corners] != " ": #Until the corner selected is empty
                corners = 2*random.randint(0,4) #Select a new corner or center
            return(corners) #Return empty corner
        else:
            sides = 2*random.randint(0,3)+1 #Selects a side
            while current_board[sides] != " ": #Until the side is empty
                sides = 2*random.randint(0,3)+1 #Selects a new side
            return(sides) #Returns empty side
    if difficulty < 4: #If difficulty is less than 4
        ran = random.randint(0,8) #Picks random spot on board
        while current_board[ran] != " ": #Until the spot is empty
            ran = random.randint(0,8) #Picks a new spot
        return(ran) #Returns empty spot

def create_victory_conditions(size): #Written by Cody West.  Not used in current program, could be used to make boards of different sizes
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
#create an example board to show players what slot numbers they can choose. Will display during the first 3 turns of the game
    example_board_vert_1 = "  1  I  2  I  3  "
    example_board_vert_2 = "  4  I  5  I  6  "
    example_board_vert_3 = "  7  I  8  I  9  "
    example_board_horiz = "_________________"
    
    print("")
    print("Here's what slots you can select:")
    print(example_board_vert_1)
    print(example_board_horiz)
    print(example_board_vert_2)
    print(example_board_horiz)
    print(example_board_vert_3)
    print("")
    

def draw_board(current_board): #By Grant
#draws the most current version of the board (current_board)

    board_vert_1 = "  "+current_board[0]+"  "+"I"+"  "+current_board[1]+"  "+"I"+"  "+current_board[2]+"  " #draws first row of slots and vertcal spacers
    board_vert_2 = "  "+current_board[3]+"  "+"I"+"  "+current_board[4]+"  "+"I"+"  "+current_board[5]+"  " #draws second row of slots and vertical spacers
    board_vert_3 = "  "+current_board[6]+"  "+"I"+"  "+current_board[7]+"  "+"I"+"  "+current_board[8]+"  " #draws third row of slots and verticalspacers
    board_horiz_1 = "_"*len(board_vert_1) #draws first horizontal spacer
    board_horiz_2 = "_"*len(board_vert_2) #draws second horizontal spacer


    print("Take your pick:")
    print(board_vert_1)
    print(board_horiz_1)
    print(board_vert_2)
    print(board_horiz_2)
    print(board_vert_3)
    print("")#print the board

def check_victory(current_board):#By Joshua Landis

    #this function is going to try to find a victory and then return a win or a tie

    WAYS_TO_WIN = [[0, 1, 2],[3, 4, 5],[6, 7, 8],[0, 3, 6],[1, 4, 7],[2, 5, 8],[0, 4, 8],[2, 4, 6]]
    #just looks neater and more intuitive :-)

    for board in WAYS_TO_WIN:
        if current_board[board[0]] == current_board[board[1]] == current_board[board[2]] and current_board[board[0]]!= (" "):#if all of the slots have the same symbol
            draw_board(current_board)
            print("IT'S OVER!")
            print(current_board[board[0]], "WINS")
            return "done"
            
        if current_board.count(" ") == 0:#if all of the spaces are filled and none have this blank value
            draw_board(current_board)
            print("IT'S OVER!")
            print("YOU'RE ALL LOSERS!")

            return "done"          #tells the function to stop when there are no blank spaces and no wins
            

def get_input (current_board, turn):
    #get_input checks that player_input is valid and returns the slot
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player_input = 0    
    while numbers.count(player_input)==0 or ((current_board[player_input])!=" "):
        player_input=int(raw_input("Where would you like to put your symbol? "))
        if numbers.count(player_input)==0:#if someone says something that isn't 1-9
            print(player_input,"Is not a valid move buddy. Try again-->")#tell them to try again

            
        else:#if it's ok
            
            player_input=player_input-1#bring it down one for the update board function
            
            if ((current_board[player_input]) == " "):#while the space the chose is empty

                print(player_input, "Is a valid move")#tell them its a valid move
                
                slot = player_input#convert the player_input into slot(the variable that the rest of the function uses

                return slot #return slot back to the rest of the function

            else:#if that spot has already been taken

                print(player_input + 1, " has already been taken. Please select another slot.")#tell them they need to pick again and the loop starts over
                
        
    
    

def update_board(current_board, slot, symbol): #By Grant
#Recives a slot value from get_input it uses to assign a section of the current_board list to the X or O of the player's selection
    current_board[slot] = symbol
    return current_board


def TicTacToe(): #Written by Cody West
    """Plays Tic Tac Toe"""
    current_board = [" "," "," "," "," "," "," "," "," "] #Empty board
    players = 0 #Number of players
    human_turn = 0 #Indicates whether the human goes first or second (is 0 for two player games)
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
        while human_turn != 1 and human_turn != 2: #While a human turn has not been chosen
            human_turn = int(raw_input("Would you like to go first (1) or second (2)?")) #Ask for human turn
            if human_turn != 1 and human_turn != 2: #If a valid turn is not chosen
                print("Please pick turn 1 or 2") #Print error message
    if human_turn == 1: #If human goes first
        player1 = "human" #Player 1 is human
        player2 = "AI" #Player 2 is AI
    elif human_turn == 2: #If human goes second
        player1 = "AI" #Player 1 is AI
        player2 = "human" #Player 2 is human
    else: #If neither
        player1 = "human" #Player 1 is human
        player2 = "human" #Player 2 is human
    while turn < 10: #While the number of turns in Tic Tac Toe has not been exceeded
        if turn < 3: #For the first three turns
            draw_example_board() #Draw a board showing the slot numbers
        draw_board(current_board) #Draw current board
        ## You could write this logic much more compactly -- try to avoid having so many
        ## lines of code that look identical. You have four different update_board calls
        ## here where you could have just one.
        if turn%2 == 1: #If it's an odd numbered turn
            if player1 == "human":
                print("human")
                update_board(current_board, get_input(current_board, turn), "X") #Update board with player 1's selection and X
            else:
                print("AI")
                update_board(current_board, AI(current_board,"X","O", difficulty), "X") #Update board with AI selection
        else:
            if player2 == "human":
                print("human")
                update_board(current_board, get_input(current_board, turn), "O") #Update board with player 2's selection and X
            else:
                print("AI")
                update_board(current_board, AI(current_board,"O","X", difficulty), "O") #Update board with AI selection
        if check_victory(current_board) == "done":
            return "whatever"#Check victory
        turn = turn + 1 #Increase turn number


TicTacToe()

