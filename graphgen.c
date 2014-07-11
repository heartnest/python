/*	##############################################################################################
	Advanced RTI System, ARTÌS			http://pads.cs.unibo.it
	Large Unstructured NEtwork Simulator (LUNES)

	Description:
		For a general introduction to LUNES implmentation please see the 
		file: mig-agents.c

		This an external tool used to build graphs that will be used
		in the simulator.

	Authors:
		First version by Gabriele D'Angelo <g.dangelo@unibo.it>

	############################################################################################### 

	TODO:

		-	Almost everything :-(

*/

#include <stdlib.h>
#include <igraph.h>


int main(int argc, char* argv[]) {
	igraph_t 		graph;
	igraph_integer_t	nodes;
	igraph_integer_t	diameter;
	igraph_bool_t		result;
	FILE			*output_dot;
	igraph_integer_t	max_diameter;
	igraph_integer_t	edges;

	if (argc != 5) {

		fprintf(stdout, "Syntax error:\n");
		fprintf(stdout, "USAGE: graphgen <# nodes> <edges> <output_file_name> <max_diameter>\n");
		fflush(stdout);
		exit (-1);
	}

	nodes = (igraph_integer_t) atoi(argv[1]);
	edges = (igraph_integer_t) atof(argv[2]);
	max_diameter = (igraph_integer_t) atoi(argv[4]);

	fprintf(stdout, "Generating a graph with %d vertices and %d edges\n", (int)nodes, (int)edges);
	fflush(stdout);
  	
	igraph_real_t cluster=0;
	igraph_real_t avgpath=0;	
	igraph_real_t cscore=0;
	while ( (int)result != 1) {

		printf(".");

		//igraph_barabasi_game(&graph, nodes, 1.0, 2/*edegs*/, 0, 0, /*A*/1.0,  IGRAPH_UNDIRECTED, IGRAPH_BARABASI_PSUMTREE,/*start from*/0);
		//igraph_erdos_renyi_game(&graph, IGRAPH_ERDOS_RENYI_GNM, nodes, edges, IGRAPH_UNDIRECTED, IGRAPH_NO_LOOPS);
		igraph_watts_strogatz_game(&graph, 1,  nodes, 2, 0.3,  0,  0);
		//igraph_growing_random_game(&graph, nodes, 2, 0, 1);
		
		igraph_simplify(&graph,1,0,0);
		igraph_is_connected(&graph, &result, 0);

		if ( (int)(result) == 0 ) {
			printf("Graph is NOT connected so do it again \n ");	
			// nothing to do
		}
		else {
			igraph_diameter(&graph, &diameter, 0, 0, 0, IGRAPH_UNDIRECTED, 1);

			if ( diameter > max_diameter ) {
				printf("diameter PROBLEM risk repeating infinitely!!! \n ");
				result = (igraph_integer_t) 0;
			}else{

				printf("diameter satisfied \n ");
			}
		}
	}


	printf("\nConnected graph? (0/1): %d\n", (int) result);
	printf("Diameter of the graph: %d\n", (int) diameter);
	printf("Number of vertices in the graph: %d\n", (int) igraph_vcount(&graph));
	printf("Number of edges in the graph: %d\n", (int) igraph_ecount(&graph));

	printf("\n **********************************************************");
        igraph_transitivity_undirected(&graph,&cluster,IGRAPH_TRANSITIVITY_NAN);
	printf("\nCluster of the graph?: %f\n", cluster);
	igraph_average_path_length(&graph,&avgpath,0,0);
	printf("Avg path length of the graph?: %f\n", avgpath);
	igraph_centralization_degree(&graph,0,IGRAPH_ALL,0,&cscore,0,1);
	printf("centralisation score of the graph?: %f", cscore);
	printf("\n **********************************************************\n");


	output_dot = fopen(argv[3], "w");

	igraph_write_graph_dot(&graph, output_dot);

	fclose(output_dot);

	igraph_destroy(&graph);

	return 0;
}

