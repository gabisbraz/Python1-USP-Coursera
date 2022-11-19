import re

def le_assinatura():
	'''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''

	print("Bem-vindo ao detector automático de COH-PIAH.")
	print("Informe a assinatura típica de um aluno infectado:")

	wal = float(input("Entre o tamanho médio de palavra: "))
	ttr = float(input("Entre a relação Type-Token: "))
	hlr = float(input("Entre a Razão Hapax Legomana: "))
	sal = float(input("Entre o tamanho médio de sentença: "))
	sac = float(input("Entre a complexidade média da sentença: "))
	pal = float(input("Entre o tamanho medio de frase: "))
	return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
	'''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
	i = 1
	textos = []
	texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
	while texto:
		textos.append(texto)
		i += 1
		texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
	return textos

def separa_sentencas(texto):
	'''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
	sentencas = re.split(r'[.!?]+', texto)
	if sentencas[-1] == '':
		del sentencas[-1]
	return sentencas

def separa_frases(sentenca):
	'''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
	return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
	'''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
	return frase.split()

def n_palavras_unicas(lista_palavras):
	'''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
	freq = dict()
	unicas = 0
	for palavra in lista_palavras:
		p = palavra.lower()
		if p in freq:
			if freq[p] == 1:
				unicas -= 1
			freq[p] += 1
		else:
			freq[p] = 1
			unicas += 1
	return unicas

def n_palavras_diferentes(lista_palavras):
	'''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
	freq = dict()
	for palavra in lista_palavras:
		p = palavra.lower()
		if p in freq:
			freq[p] += 1
		else:
			freq[p] = 1
	return len(freq)

def tracos_linguisticos_palavras(palavras_totais, palavras_diferentes, palavras_unicas):
	#Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras
	tamanho_total = 0
	for palavra in palavras_totais:
		t = len(palavra)
		tamanho_total += t
	tamanho_medio_palavra = tamanho_total / len(palavras_totais)
	#Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras
	type_token = palavras_diferentes / len(palavras_totais)
	#Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido pelo total de palavras.
	hapax_legomana = palavras_unicas / len(palavras_totais)
	return [tamanho_medio_palavra, type_token, hapax_legomana]

def tracos_linguisticos_sentencas_frases(sentencas_totais, frases_totais):
	#Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças
		#(os caracteres que separam uma sentença da outra não devem ser contabilizados como parte da sentença).
	tamanho_medio_sentenca = 0
	for sentenca in sentencas_totais:
		for caractere in sentenca:
			tamanho_medio_sentenca += 1
	tamanho_medio_sentenca = tamanho_medio_sentenca / len(sentencas_totais)
	#Complexidade de sentença é o número total de frases divido pelo número de sentenças.
	complexidade_sentenca = len(frases_totais) / len(sentencas_totais)
	#Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto
		# (os caracteres que separam uma frase da outra não devem ser contabilizados como parte da frase).
	tamanho_medio_frase = 0
	for frase in frases_totais:
		for caractere in frase:
			tamanho_medio_frase += 1
	tamanho_medio_frase = tamanho_medio_frase / len(frases_totais)
	return [tamanho_medio_sentenca, complexidade_sentenca, tamanho_medio_frase]

def calcula_assinatura(texto):
	'''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
	palavras_totais = []
	sentencas_totais = []
	frases_totais = []
	lista_sentencas = separa_sentencas(texto)
	sentencas_totais += lista_sentencas
	for sentenca in lista_sentencas:
		lista_frases = separa_frases(sentenca)
		frases_totais += lista_frases
		for frase in lista_frases:
			lista_palavras = separa_palavras(frase)
			palavras_totais += lista_palavras
		palavras_unicas = n_palavras_unicas(palavras_totais)
		palavras_diferentes = n_palavras_diferentes(palavras_totais)
		tamanho_medio_palavra, type_token, hapax_legomana = tracos_linguisticos_palavras(palavras_totais, palavras_diferentes, palavras_unicas)
		tamanho_medio_sentenca, complexidade_sentenca, tamanho_medio_frase = tracos_linguisticos_sentencas_frases(sentencas_totais, frases_totais)
	tracos_linguisticos = [tamanho_medio_palavra, type_token, hapax_legomana, tamanho_medio_sentenca, complexidade_sentenca, tamanho_medio_frase]
	return tracos_linguisticos

def compara_assinatura(as_a, as_b):
	'''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
	#a: entrada
	#b: texto
	S = 0
	for i in range(len(as_a)):
		S += abs(as_a[i] - as_b[i])
	S = S / 6
	print(2, S)
	return S

def avalia_textos(textos, ass_cp):
	'''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
	compara = []
	for texto in textos:
		as_b = calcula_assinatura(texto)
		s = compara_assinatura(ass_cp, as_b)
		compara.append(s)
	copiado = min(compara)
	for i in range(len(textos)):
		if compara[i] == copiado:
			return i + 1

def main():
	as_a = le_assinatura()
	textos = le_textos()
	num_texto = avalia_textos(textos, as_a)
	print("O autor do texto {} está infectado com COH-PIAH" .format(num_texto))

main()