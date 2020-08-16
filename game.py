from random import getrandbits

# player_count = 5
player_count = int(input("How many players\n"))
# tries = 2
tries = int(input("How many maximum tries for one player per move\n"))
lost = 5
players = [0 for q in range(player_count)]
move = 0

print()

while lost not in players and move < 1000:
	move += 1
	print('--move_{}--\n'.format(move))

	for i in range(len(players)):
		print('player #{}'.format(i + 1))

		for j in range(tries):
			scored = getrandbits(1)
			if scored == 1:
				print('score!')
				break
			else:
				print('missed')

		if scored == 0:
			players[i] += 1
			print("{}\n".format(players[i]))
		else:
			print("{}\n".format(players[i]))

		if players[i] == lost:
			print('\nplayer #{} lost\n\ton move {}'.format(i + 1, move))
			break
	else:
		input("Press enter to continue... ")
		continue
	break
else:
	if move < 1000:
		print("count of moves became higher than 1000")
