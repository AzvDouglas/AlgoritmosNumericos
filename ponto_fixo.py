#=====================================================
import funcao_iteracao

def ponto_fixo(epsilon,MaxIter):
	Iter = 1
	x0=0.5
	while Iter <= MaxIter:
		#iteracao do ponto fixo
		x = funcao_iteracao(x0)  			
		erro_abs = abs(x-x0)
		#condicao de parada 
		if erro_abs < epsilon:
			print('\nNumero de iteracoes:',Iter) 
			print('\nSolucao aproximada:',x)
			return 	
		#atualizacao das variaveis 
		Iter = Iter+1 
		x0 = x 
		      	
	else:
		print('ERRO: Numero maximo de iteracoes excedido!')

epsilon_teste = 0.0001
MaxIter_teste = 100
ponto_fixo(epsilon_teste,MaxIter_teste)

#=====================================================

