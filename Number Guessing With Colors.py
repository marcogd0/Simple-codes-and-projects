from random import randrange

Computador = randrange(1000)

while True:
	Jogador = int(input())
	if Computador == Jogador:
		print("You win!")
		break
	#if Computador < Jogador:
		#print("\033[1;31mSmaller\033[m")
	else:
		#print("\033[1;32mBigger\033[m")
		print("\033[4;31mSmaller\033[m") if Computador < Jogador else print("\033[4;32mBigger\033[m")