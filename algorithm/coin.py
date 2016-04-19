import glob
import sys
import math



def printMatrix(V,testMatrix):
	print "----------------------"
	for i, row in enumerate(testMatrix):
		if i-1 >=0:
			print V[i-1],' '.join([str(y) for y in row])
		else:
			print ' ',' '.join([str(y) for y in row])
		


def _get_change_making_matrix(V, S):
	""" make a matrix [0,1,2,3,...,S][0,0,0 ..., 0][0,0,0 ..., 0] """
	m = [[0 for _ in range(S + 1)] for _ in range(len(V) + 1)]
	
	for i in range(S + 1):
		m[0][i] = i
	print m
	return m
  
def change_making(V, S):

	"""This function assumes that all coins are available infinitely.
 
    n is the number that we need to obtain with the fewest number of coins.
 
    coins is a list or tuple with the available denominations."""
	m = _get_change_making_matrix(V, S)
	for c in range(1, len(V) + 1):
		for r in range(1, S + 1):

			# Just use the coin coins[c - 1].
			if V[c - 1] == r:
				m[c][r] = 1




            # coins[c - 1] cannot be included.
            # We use the previous solution for making r,
            # excluding coins[c - 1].
            
			elif V[c - 1] > r:
				m[c][r] = m[c - 1][r]




            # We can use coins[c - 1].
             # We need to decide which one of the following solutions is the best:
             # 1. Using the previous solution for making r (without using coins[c - 1]).
             # 2. Using the previous solution for making r - coins[c - 1] (without using coins[c - 1])
             # plus this 1 extra coin.
            
			else:
				m[c][r] = min(m[c - 1][r], 1 + m[c][r - V[c - 1]]) 


			printMatrix(V,m)
            
        
	return m[-1][-1]





V = [2]
S = 6

test = change_making(V, S)

print "final result:", test