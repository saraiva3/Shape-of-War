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

#https://networkx.github.io/documentation/networkx-1.10/reference/algorithms.clustering.html


#QUESTAO E 
# components = networkx.connected_components(networkx.from_numpy_matrix(numpy.matrix(temp_A)))
# For the time being returns the size of the largest component
#component_sizes = [len(x) for x in components][0]



#QUESTAO F

#https://stackoverflow.com/questions/49733244/how-can-i-calculate-neighborhood-overlap-in-weighted-network


#QUESTAO G

#https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.algorithms.shortest_paths.generic.average_shortest_path_length.html

#QUESTAO H

#https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.algorithms.centrality.betweenness_centrality.html
#https://networkx.github.io/documentation/networkx-1.9/reference/generated/networkx.algorithms.centrality.edge_betweenness_centrality.html


#QUESTAO I

#https://networkx.github.io/documentation/latest/_modules/networkx/algorithms/bridges.html

#QUESTAO J

#https://networkx.github.io/documentation/networkx-1.9.1/reference/algorithms.assortativity.html

#QUESTAO K, visualizacao