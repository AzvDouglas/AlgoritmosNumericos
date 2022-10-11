#=====================================================

def bissecao(a,b,epsilon,MaxIter):
	Iter = 1
	fa = funcao(a)	
	while Iter <= MaxIter:
		#iteracao da bissecao
		x = (a + b)/2  
		fx = funcao(x)		
		erro_abs = abs(b-a)/2
		#condicao de parada 
		if erro_abs < epsilon:
			print('\nNumero de iteracoes:',Iter) 
			print('\nSolucao aproximada:',x)
			return 	
		#bissecta o intervalo  
		Iter = Iter+1  
		if fa*fx < 0: 
			b = x  
		else: 
			a = x  
			fa = fx      	
	else:
		print('ERRO: Numero maximo de iteracoes excedido!')
#=====================================================
