# Dynamic Programming Python implementation of Coin Change problem
""" ref: http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/ """


def printMatrix(testMatrix):
    print "----------------------"
    for i, row in enumerate(testMatrix):
            print ' ',' '.join([str(y) for y in row])


def count(V, m, S):
    # We need n+1 rows as the table is consturcted in bottom up
    # manner using the base case 0 value case (n = 0)
    table = [[0 for x in range(m)] for x in range(S+1)]
 
    # Fill the enteries for 0 value case (n = 0)
    for i in range(m):
        table[0][i] = 1
 

    printMatrix(table)
    # Fill rest of the table enteries in bottom up manner
    for i in range(1, S+1):
        for j in range(m):
            # Count of solutions including S[j]
            x = table[i - V[j]][j] if i-V[j] >= 0 else 0
 
            # Count of solutions excluding S[j]
            y = table[i][j-1] if j >= 1 else 0
 
            # total count
            table[i][j] = x + y
            printMatrix(table)
 
    return table[S][m-1]
 
# Driver program to test above function
V = [3, 1, 4]
m = len(V)
S = 0
print(count(V, m, S))
 
# This code is contributed by Bhavya Jain