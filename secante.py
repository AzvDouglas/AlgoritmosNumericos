#=====================================================
def secante(a,b,epsilon,MaxIter):
	Iter = 1
	fa = funcao(a)
	fb = funcao(b)
	while Iter <= MaxIter:
		#iteracao da secante
		x = b - fb*(b-a)/(fb - fa)
		fx = funcao(x)
		erro_abs = abs(x-b)
		#condicao de parada 
		if erro_abs < epsilon:
			print('\nNumero de iteracoes:',Iter) 
			print('\nSolucao aproximada:',x)
			return 	
		#atualizacao das variaveis 
		Iter = Iter+1 
		a = b
		b = x
		fa =fb
		fb = fx		      	
	else:
		print('ERRO: Numero maximo de iteracoes excedido!')
#=====================================================

