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
    if AI(boarde, "x", "o") != 6:
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
        for i in range(len(slots)): 
            check.append(current_board[slots[i]])
        if check.count(AI_symbol)==2 and check.count(" ")==1:
            return(slots[check.index(" ")])
    


def draw_board(current_board):


def check_victory(current_board):



def update_board(current_board, slot, symbol):
