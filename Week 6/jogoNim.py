def campeonato():
	ganhadorU = 0
	ganhadorC = 0
	for i in range(3):
		print("**** Rodada {} ****" .format(i))
		resultado = partida()
		if resultado == "Você ganhou!":
			ganhadorU += 1
		elif resultado == "Erro":
			return "Erro"
		else:
			ganhadorC += 1
	return ganhadorU , ganhadorC
####################################################################
def partida():
	while True:
		n = int(input("Quantas peças? "))
		m = int(input("Limite de peças por jogada? "))
		if n <= m:
			return "Erro"
		if n % (m + 1) == 0:
			print("Você começa!")
			while True:
				u = usuario_escolhe_jogada(n, m)
				n = n - u
				if n == 0:
					return "Você ganhou!"
				else:
					print("Sobraram {} peças!\nComputador jogando..." .format(n))
				c = computador_escolhe_jogada(n, m)
				n = n - c
				if n == 0:
					return "O computador ganhou!"
				else:
					print("Sobraram {} peças!" .format(n))

		else:
			print("Computador começa!")
			while True:
				c = computador_escolhe_jogada(n, m)
				n = n - c
				if n == 0:
					return "O computador ganhou!"
				else:
					print("Sobraram {} peças!" .format(n))
				u = usuario_escolhe_jogada(n, m)
				n = n - u
				if n == 0:
					"Você ganhou!"
				else:
					print("Sobraram {} peças!\n Computador jogando..." .format(n))

####################################################################
def computador_escolhe_jogada(n, m):
	for i in range(1, m + 1):
		tentativa = n - i
		if tentativa % (m + 1) == 0:
			return i
	return m
####################################################################
def usuario_escolhe_jogada(n, m):
	while True:
		usuario = int(input("Quantas peças você vai tirar? "))
		if usuario > m or usuario >= n:
			print("Oops! Jogada inválida! Tente de novo.")
		else:
			return usuario
#####################################################################
def main():
	while True:
		start = input("Bem-vindo ao jogo do NIM! Escolha:\n"
								"1 - para jogar uma partida isolada\n"
								"2 - para jogar um campeonato\n")
		if start == "1":
			print("Voce escolheu uma partida isolada!")
			print(partida())
			break
		elif start == "2":
			print("Voce escolheu um campeonato!")
			placar = campeonato()
			if placar == "Erro":
				print("Algo deu errado! Por favor, recomece!")
			else:
				print("**** Final do campeonato! ****\nPlacar: Você {} X {} Computador" .format(placar[0], placar[1]))
			break

main()


