"""
[17/2/2015] Siano date due stringhe P = p1p2...pm e 
T = t1t2...tn di caratteri alfabetici. 
Si progetti un algoritmo di "programmazione dinamica" 
per individuare la piu lunga sottosequenza
comune tra P e T (per esempio, 
se P = 9,15,3,6,4,2,5,10,3 e T = 8,15,6,7,9,2,11,3,1 
allora il risultato e: 15, 6, 2, 3).

original ref: https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Longest_common_subsequence
modified by Tong

"""

# original LCS
# def LCS(X, Y):
#     m = len(X)
#     n = len(Y)
#     # An (m+1) times (n+1) matrix
#     C = [[0] * (n + 1) for _ in range(m + 1)]
#     for i in range(1, m+1):
#         for j in range(1, n+1):
#             if X[i-1] == Y[j-1]: 
#                 C[i][j] = C[i-1][j-1] + 1
#             else:
#                 C[i][j] = max(C[i][j-1], C[i-1][j])
#     return C

def lcs(X, Y):
    m = len(X)
    n = len(Y)
    C  = []

    for i in range(m+1):
        arr1 = []
        for j in range(n+1):
            arr = ""
            arr1.append(arr)
        C.append(arr1)

    print C
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]: 
                C[i-1][j-1] += str(X[i-1])+","
                C[i][j] =C[i-1][j-1]
            else:
                print C[1][3]
                if len(C[i][j-1]) > len(C[i-1][j]):
                    C[i][j] = C[i][j-1]
                    print i,' ',j,' ',i,' ',j-1,  C[i][j]
                else:
                    C[i][j] = C[i-1][j]
                    print i,' ',j,' ',i-1,' ',j,  C[i][j]
    return C[-1][-1]

a = [9,15,3,6,4,2,5,10,3]
b = [8,15,6,7,9,2,11,3,1]
res = lcs(a, b)
print res