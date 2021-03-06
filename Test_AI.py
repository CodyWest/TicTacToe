def AI(current_board, AI_symbol, opponent_symbol):
    victory_conditions = [[0,4,8],[2,4,6],[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8]]
    for n in range(len(victory_conditions)):
        slots = victory_conditions[n]
        check = []
        for i in range(len(slots)):
            check.append(current_board[slots[i]])
            if check.count(AI_symbol)==2 and check.count(" ")==1:
                return(slots[check.index(" ")])


def test_AI():
    boarda = [“ “,“ “,“ “,“ “,“ “,“ “,“ “,”x”,”x”]
    boardb =  [“o“,“o“,“ “,“ “,“ “,“ “,“ “,” ”,” ”]
    boardc =  [“o“,“o“,“ “,“ “,“ “,“ “,“ “,”x”,”x”]
    boardd = [“ “,“ “,“ “,“ “,“ “,“ “,“ “,” ”,” ”]
    boarde = [“x“,“o“,“ “,“ “,“ “,“ “,“ “,” ”,” ”]
    if AI(boarda, “x”, ”o”) != 6:
        print(“Error on board a”)
    if AI(boardb, “x”, ”o”) != 2:
        print(“Error on board b”)
    if AI(boardc, “x”, ”o”) != 6:
        print(“Error on board c”)
    if AI(boardd, “x”, ”o”) != 4:
        print(“Error on board d”)
    if AI(boarde, “x”, ”o”) != 6:
        print(“Error on board e”)


print(test_AI())
