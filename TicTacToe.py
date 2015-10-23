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
     

def AI(current_board, AI_symbol, opponent_symbol):
    """Chooses moves for computer based on state of current board"""
    victory_conditions = [[0,4,8],[2,4,6],[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8]] #Establishes victory conditions to be checked
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
    for n in range(len(victory_conditions)): #For each victory condition in victory_conditions
        slots = victory_conditions[n] #Take the victory conditions and put them in a new list
        check = [] #Creates empty folder called check
        for i in range(len(slots)): #For each spot in slots
            check.append(current_board[slots[i]]) #Add the corresponding spot from the current board to check
        if check.count(AI_symbol)==1 and check.count(" ")==2: #If there are any rows where the AI has one symbol and there's two empty spots
            if check[0] == " ":
                return(slots[0])
            else:
                return(slots[2])
    if current_board[4] == " ":
        return(4)
    else:
        return(0)
                    
    
    
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
    board_vert = "____________________"

def check_victory(current_board):
    print("lol")


def update_board(current_board, slot, symbol):
    print("lol")

#test the stuff!
for x in range (0,3):
    draw_example_board()
    print""
