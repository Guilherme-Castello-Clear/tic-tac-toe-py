moves = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
game_on = True
current_turn = 'X'


def check_labels(index1, index2, index3):
	global game_on
	if moves[index1] == moves[index2] and moves[index1] == moves[index3]:
		game_on = False
		print_table()
		print(f'{current_turn} Wins!')


def validade():
	check_labels(0, 1, 2)
	check_labels(3, 4, 5)
	check_labels(6, 7, 8)


def is_available(selected):
	for move in moves:
		if move == selected:
			moves[int(selected)] = current_turn
			return True


def print_table():
	print(f'\n\n\n{moves[0:3]}\n{moves[3:6]}\n{moves[6:9]}')


while game_on:
	print_table()
	print(f'Current turn: {current_turn}')

	selected = input("Choose your move: ")
	if not is_available(selected):
		print('Invalid movement!')
	else:
		validade()
		if current_turn == 'X':
			current_turn = 'O'
		else:
			current_turn = 'X'
