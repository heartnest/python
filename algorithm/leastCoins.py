""" playground for dynamic programming, coin making problem 

Problema:
Data un insieme di valori di monete V1,...,Vm e un valore S. 
Determinare il numero minimo di monete necessarie per pagare una somma S. 
Utilizzare la programmazione dinamica

Modified by Tong Liu

ref: https://en.wikipedia.org/wiki/Change-making_problem """



def printMatrix(V,testMatrix):
	print "----------------------"
	for i, row in enumerate(testMatrix):
		if i-1 >=0:
			print V[i-1],' '.join([str(y) for y in row])
		else:
			print ' ',' '.join([str(y) for y in row])
		


def _get_change_making_matrix(V, S):
	""" make a matrix [0,1,2,3,...,S][0,0,0 ..., 0][0,0,0 ..., 0] """
	T = [[0 for _ in range(S + 1)] for _ in range(len(V) + 1)]
	
	for i in range(S + 1):
		# T[0][i] =  float("inf") #correct version
		T[0][i] =  i # illustration purpose
	print T
	return T
  
def change_making(V, S):

	"""This function assumes that all coins are available infinitely.
 
    n is the number that we need to obtain with the fewest number of coins.
 
    coins is a list or tuple with the available denominations."""
	T = _get_change_making_matrix(V, S)
	for c in range(1, len(V) + 1):
		for r in range(1, S + 1):

			# Just use the coin V[c - 1].
			if V[c - 1] == r:
				T[c][r] = 1

            # V[c - 1] cannot be included.
            # We use the previous solution for making r,
            # excluding V[c - 1].
            
			elif V[c - 1] > r:
				T[c][r] = T[c - 1][r]

            # We can use V[c - 1].
             # We need to decide which one of the following solutions is the best:
             # 1. Using the previous solution for making r (without using V[c - 1]).
             # 2. Using the previous solution for making r - V[c - 1] (without using V[c - 1])
             # plus this 1 extra coin.
            
			else:
				T[c][r] = min(T[c - 1][r], 1 + T[c][r - V[c - 1]]) 


			printMatrix(V,T)
            
        
	return T[-1][-1]





V = [2,3,6,11]
S = 8

test = change_making(V, S)

print "final result:", test