import networkx as nx
import matplotlib
matplotlib.use ("agg")
import matplotlib . pyplot as plt




GraphFile = "graphs/ONLY_RED.graphml"

G = nx.read_graphml(GraphFile)


#QUESTAO B
#DISTRIBUICAO DOS GRAUS
degrees = {}

for node in G.nodes():
	single_degree = G.degree(node)
	if single_degree not in degrees:
		degrees[single_degree] = 0
	degrees[single_degree] += 1

degrees_map = sorted(degrees.items())

#FAZER POWER LAW DOS NEGATIVOS

#https://stackoverflow.com/questions/30077957/calculate-the-degree-of-nodes-only-including-edges-with-a-specific-attribute-in

fig = plt.figure()
ax = fig.add_subplot(111)
ax.loglog([ degree for (degree , frequency ) in degrees_map ] , [ frequency for (degree ,frequency ) in degrees_map ],  'red')
plt.legend("Combatants")
plt.xlabel('Degree')
plt.ylabel('Number of nodes')
plt.title ( "Degree Distribution of Combatants" )

plt.xlim([2*10**0, 2*10**2])
fig.savefig ( "degree_distribution_red.png" )

#GRAU MEDIO
sum_of_edges = 0
for node in G.nodes():
	sum_of_edges += G.degree(node)

average_degree = sum_of_edges/len(G)

print(average_degree)


#QUESTAO C

print(nx.number_connected_components(G))

#QUSTAO D

clustering = {}
index = 0
for node in G.nodes():
	clustering[index] = nx.clustering(G,node)	
	index = index + 1 

degrees_map = sorted(clustering.items())



#QUESTAO E 
# components = networkx.connected_components(networkx.from_numpy_matrix(numpy.matrix(temp_A)))
# For the time being returns the size of the largest component	
#component_sizes = [len(x) for x in components][0]



#QUESTAO F

#https://stackoverflow.com/questions/49733244/how-can-i-calculate-neighborhood-overlap-in-weighted-network

overlap = {}

for node1 in G.nodes():
	for node2 in G.nodes():
		if(nx.has_edge(G,node1, node2))
			n_common_nbrs = len(set(nx.common_neighbors(G, node1, node2)))
			n_join_nbrs = g.degree(node1) + g.degree(node2) - n_common_nbrs - 2
			result = n_common_nbrs/n_join_nbrs
			if result not in overlap:
				overlap[result] = 0
			overlap[result] += 1

overlap_map = sorted(overlap.items())
#QUESTAO G

#https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.algorithms.shortest_paths.generic.average_shortest_path_length.html


average_short_path = nx.average_shortest_path_length(G)
shortpath = {}
for node1 in G.nodes:
	for node2 in G.nodes:
		path_len = nx.shortest_path_length(G, node1, node2)
		if path_len not in shortpath:
			shortpath[path_len] = 0
		shortpath[path_len] += 0

		
shortpath_map = sorted(shortpath.items())
#QUESTAO H

#https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.algorithms.centrality.betweenness_centrality.html
#https://networkx.github.io/documentation/networkx-1.9/reference/generated/networkx.algorithms.centrality.edge_betweenness_centrality.html


#QUESTAO I

#https://networkx.github.io/documentation/latest/_modules/networkx/algorithms/bridges.html

#QUESTAO J

#https://networkx.github.io/documentation/networkx-1.9.1/reference/algorithms.assortativity.html
