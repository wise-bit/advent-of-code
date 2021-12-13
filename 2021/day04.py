'''
@Author: wise-bit
@Date: 2021-12-XX
'''

sep = "\n" # separator
c = 0 # counter

boards = []
calls = []
called = 0


def bingoWin(board):
	for i in range(5):
		count = 0
		for j in range(5):
			if board[i][j][1] == 1:
				count += 1
		if count == 5: 
			return True

	for i in range(5):
		count = 0
		for j in range(5):
			if board[j][i][1] == 1:
				count += 1
		if count == 5: 
			return True

	return False



with open('input.txt', 'r') as file:
	inp = file.read().split(sep)
	# print(i)
	
	calls = list(map(int, inp[0].split(",")))

	# print(calls)

	totalBoards = (len(inp) - 1) // 6

	# print(totalBoards)

	board = []
	for i in range(2, len(inp)+1):
		if (i-1)%6 == 0:
			boards.append(board)
			board = []
			continue

		line = [[x, 0] for x in list(map(int, inp[i].strip().split()))]
		board.append(line)

# print(boards)

def scoreBoard(board):
	zeros = 0
	ones = 0

	for i in range(5):
		for j in range(5):
			if board[i][j][1] == 0:
				zeros += board[i][j][0]
			else:
				ones += board[i][j][0]

	# print(zeros, ones)

	return zeros



currentPos = 0
winnerFound = False
winnerBoard = []

lastWinner = []

def updateBoard(board, val):
	for i in range(5):
		for j in range(5):
			if board[i][j][0] == val:
				board[i][j][1] = 1


while (currentPos < len(calls) and not winnerFound):
	numCall = calls[currentPos]
	# print(numCall)
	for board in boards:
		updateBoard(board, numCall)

	for board in boards:
		if bingoWin(board):
			# winnerBoard = board
			# winnerFound = True
			lastWinner = board
			boards.remove(board)
			# print(board)
			# break

	if (winnerFound):
		print(scoreBoard(winnerBoard), calls[currentPos])
		print(scoreBoard(winnerBoard) * calls[currentPos])


	if (len(boards) == 0): break

	currentPos += 1


# print(lastWinner, calls[currentPos])
print(scoreBoard(lastWinner) * calls[currentPos])
