""" 
playground for dynamic programming, number of coin combinations for sum S  

Problema:
Data un insieme di monete V1,...,Vm e un valore S. 
Determinare il numero di combinazione possibile per pagare 
una somma S senza dare il resto. Utilizzare la programmazione dinamica.

Modified by Tong Liu

ref: http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/ 
"""


def printMatrix(V,testMatrix):
	print "----------------------"
	for i, row in enumerate(testMatrix):
		print V[i],': ',' '.join([str(y) for y in row])


# Dynamic Programming Python implementation of Coin Change problem
def countSolutions(V, n, S):
    # We need S+1 columns as the T is consturcted in bottom up
    # manner using the base case 0 value case (S = 0)
    T = [[0 for x in range(S+1)] for x in range(n)]
 
    # Fill the enteries for 0 value case (S = 0)
    for i in range(n):
        T[i][0] = 1

    # debug use
    printMatrix(V,T)
 
    # Fill rest of the T enteries in bottom up manner
    for i in range(0, n):
        for j in range(1,S+1):
            # Count of solutions including V[i]
            x = T[i][j-V[i]] if j-V[i] >= 0 else 0

            # Count of solutions excluding V[i]
            y = T[i-1][j] if i >= 1 else 0
 
            # total count
            T[i][j] = x + y
            printMatrix(V, T)
 

    return T[n-1][S]
 

# Main
V = [3,2,1]
n = len(V)
S = 3

res = countSolutions(V, n, S)
print 'Final result: ',res