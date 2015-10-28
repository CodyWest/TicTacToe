print "Turn number " + str(move+1)
		if move % 2 == 0:
			turn = 'X'
		else:
			turn = 'O'#make 

		# Get player input
		user = get_input(turn)
		while board[user] != -1:
			print "Invalid move! Cell already taken.\n Please try again.\n"
			player = get_input(turn)
		play_slots[player] = 1 if turn == 'X' else 0
