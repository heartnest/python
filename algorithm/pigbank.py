""" 
playground for dynamic programming. 
Given a total weight(coins), guess the least value of the coins in piggy bank could make.

Problema:
[19/6/2015] Per comprarvi l'ultimo gadget tecnologico, avete risparmiato
 inserendo monete in un salvadanaio. Purtroppo non avete tenuto i conti,
  e non sapete quanti soldi ci sono dentro. E' facile ottenere il valore
   totale rompendo il salvadanaio, ma sarebbe un peccato romperlo senza 
   essere sicuri che ci siano abbastanza soldi per il vostro gadget. 
   Fortunatamente, avete a disposizione le seguenti informazioni: 
   il peso totale T delle monete contenute nel salvadanaio, 
   il vettore dei pesi p[1...n] e quello dei valori v[1...n], 
   dove p[i] e' il peso in grammi e v[i] e' il valore in centesimi dell'i-esimo 
   tipo di moneta fra gli n tipi di monete prodotti nel vostro stato. 
   Scrivere in pseudocodice un algoritmo che restituisca il minimo valore 
   in centesimi che puo' essere contenuto nel salvadanaio, e valutarne la complessita'. 
   Per esempio, supponete che il peso totale sia 50 grammi, e le monete a 
   disposizione siano quella da 200 centesimi, che pesa 50 grammi, e quella da 50 centesimi, 
   che pesa 10 grammi. E' pos- sibile ottenere i 50 grammi del peso totale con una 
   singola moneta da 200 centesimi, o con 5 da 50 centesimi per un totale di 250 centesimi. 
   Quindi il valore da restituire e' 200, che e' il minimo fra i due totali.


"""


# Dynamic Programming - Memoization Technique
def salvadanaio(P,V,t,i,M):
    if t < 0:
        return 99999999
    if i==0 and t > 0:
        return 99999999
    if t == 0:
        return 0

    M = [[None for x in range(t+1)] for y in range(i+1)] 

    # value made with the first 'i' coins which weight 't' totally
    if M[i][t] is None:
        r1 = salvadanaio(P, V, t - P[i], i, M)+V[i]
        print 'r1 ',r1
        r2 = salvadanaio(P, V, t, i - 1, M)
        print 'r2 ',r2
        M[i][t] = min(r1, r2)

    return M[i][t]
 

# Main
P = [0,10,50]
V = [0,50,200]
t = 50
i = 2
M = None

res = salvadanaio(P,V,t,i,M)
print '--------------------'
print 'Final result: ',res
print '--------------------'