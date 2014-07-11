import sys
from igraph import *

#============================
# Graph gen function
#============================

def genGraphFile(nth_file):
	isConnected = False

	while isConnected == False:
		
		#Erdos_Renyi(n, p, m, directed=False, loops=False)
		g = Graph.Erdos_Renyi(n=100, m=230,directed=False, loops=False)

		#Barabasi(n, m, outpref=False, directed=False, power=1, zero_appeal=1, implementation="psumtree", start_from=None)
		#g = Graph.Barabasi(n=100, m=2, outpref=False, directed=False, power=1, zero_appeal=1, implementation="psumtree", start_from=None)

		#Watts_Strogatz(dim, size, nei, p, loops=False, multiple=False)
		#g = Graph.Watts_Strogatz(dim=1, size = 10, nei = 1, p = 0, loops=False, multiple=False)

		#Growing_Random(n, m, directed=False, citation=False)
		#g = Graph.Growing_Random(n=100, m=2, directed=False, citation=True)

		g = g.simplify()

		isConnected = g.is_connected()


	diameter = g.diameter(directed=False)
	edges = g.ecount()
	vertices = g.vcount();

	print ' =================================== '
	print 'diameter: ',diameter, ' edeges: ',edges, ' vertices: ', vertices
	print ' =================================== '

	g.write_dot('corpus/test'+str(nth_file)+'.dot')


#============================
# Main
#============================

number_of_graphs = 1

if len(sys.argv) > 1:
	number_of_graphs = int(sys.argv[1]);
	print 'Number of graphs is set to be',number_of_graphs

for index in range(0,number_of_graphs):
	genGraphFile(index)