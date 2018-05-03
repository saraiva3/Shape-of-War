import networkx as nx
import matplotlib
matplotlib.use ("agg")
import matplotlib . pyplot as plt

money = 0.01
for _ in range(27):
	money *=2
print(money)


GraphFile = "graphs/graph_version6.gexf"

G = nx.read_gexf(GraphFile)


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
ax.loglog([ degree for (degree , frequency ) in degrees_map ] , [ frequency for (degree ,frequency ) in degrees_map ],  'b.')
plt.legend('All Nodes')
plt.xlabel('Degree')
plt.ylabel('Number of nodes')
plt.title ( "Degree Distribution of nodes" )

plt.xlim([2*10**0, 2*10**2])
fig.savefig ( "degree_distribution_green.png" )

#GRAU MEDIO
sum_of_edges = 0
for node in G.nodes():
	sum_of_edges += G.degree(node)

average_degree = sum_of_edges/len(G)
print("Grau medio")
print(average_degree)


#QUESTAO C


#QUSTAO D

#clustering = {}
#index = 0
#for node in G.nodes():
#	clustering[index] = nx.clustering(G,node)	
#	index = index + 1 

#degrees_map = sorted(clustering.items())



#QUESTAO E 
# components = networkx.connected_components(networkx.from_numpy_matrix(numpy.matrix(temp_A)))
# For the time being returns the size of the largest component	
#component_sizes = [len(x) for x in components][0]
tempgraph = G.copy();

# Try to see if the graph is not connected because of isolated nodes
isolate_list = list(nx.isolates(tempgraph))
self_edges = list(nx.nodes_with_selfloops(tempgraph))

for loop in self_edges:
	tempgraph.remove_edge(loop,loop)

for isolated_node in isolate_list:
	tempgraph.remove_node(isolated_node)

subgraphs = list(nx.connected_component_subgraphs(tempgraph))
distribution_componnets={};

for sb in subgraphs:            
    size = len(sb)
    if size not in distribution_componnets:
    	distribution_componnets[size] = 0
    distribution_componnets[size] += 1




components_map = sorted(distribution_componnets.items())


fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.loglog([ degree for (degree , frequency ) in components_map ] , [ frequency for (degree ,frequency ) in components_map ],  'b.')
plt.legend('All Nodes')
plt.xlabel('Tamanho do Componente')
plt.ylabel('Number of nodes')
plt.title ( "Distribuição do tamanho dos componentes" )


fig2.savefig ( "components.png" )

print("Numero de componentes")
print(nx.number_connected_components(tempgraph 	))
#QUESTAO F

#https://stackoverflow.com/questions/49733244/how-can-i-calculate-neighborhood-overlap-in-weighted-network

overlap = {}

for node1 in G.nodes():
	for node2 in G.nodes():
		if(G.has_edge(node1, node2)):
			n_common_nbrs = len(set(nx.common_neighbors(G, node1, node2)))
			n_join_nbrs = G.degree(node1) + G.degree(node2) - n_common_nbrs - 2
			result = n_common_nbrs/n_join_nbrs
			if result not in overlap:
				overlap[result] = 0
			overlap[result] += 1
			#print("TESTE")

overlap_map = sorted(overlap.items())

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.loglog([ degree for (degree , frequency ) in overlap_map ] , [ frequency for (degree ,frequency ) in overlap_map ],  'b.')
plt.legend('All Nodes')
plt.xlabel('Overlap')
plt.ylabel('Number of nodes')
plt.title ( "Distribuição do overlap da vizinhança " )

print("Calculando Overlap")

fig2.savefig ( "overlap.png" )

#QUESTAO G

#https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.algorithms.shortest_paths.generic.average_shortest_path_length.html


#average_short_path = nx.average_shortest_path_length(G)
#shortpath = {}
#for node1 in G.nodes:
##		path_len = nx.shortest_path_length(G, node1, node2)
#		if path_len not in shortpath:
#			shortpath[path_len] = 0
#		shortpath[path_len] += 0

tempgraph = G.copy();

# Try to see if the graph is not connected because of isolated nodes
isolate_list = list(nx.isolates(tempgraph))
self_edges = list(nx.nodes_with_selfloops(tempgraph))

for loop in self_edges:
	tempgraph.remove_edge(loop,loop)

for isolated_node in isolate_list:
	tempgraph.remove_node(isolated_node)
print("Caminho Medio")
print(nx.average_shortest_path_length(tempgraph))
        # Compute the average shortest path for each subgraph and mean it!
#subgraphs = nx.connected_component_subgraphs(tempgraph)
#average=0;
#for sb in subgraphs:            
 #   average+=nx.average_shortest_path_length(sb);
        

	
#print()
node_betwenness = nx.betweenness_centrality(G)
betwenness = {}
for key,value in node_betwenness.items():
	
	if value not in betwenness:
		betwenness[value] = 0
	betwenness[value] += 1

betwenness_map = sorted(betwenness.items())
print(betwenness_map)




fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.loglog([ degree for (degree , frequency ) in betwenness_map ] , [ frequency for (degree ,frequency ) in betwenness_map ],  'b.')
plt.legend('All Nodes')
plt.xlabel('Overlap')
plt.ylabel('Number of nodes')
plt.title ( "Distribuição do overlap da vizinhança " )

print("Calculando Overlap")

fig2.savefig ( "betwenness_nos.png" )


edge_betwenness = nx.edge_betweenness_centrality(G)
betwenness = {}
for key,value in edge_betwenness.items():
	
	if value not in betwenness:
		betwenness[value] = 0
	betwenness[value] += 1

betwenness_map = sorted(betwenness.items())






fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.loglog([ degree for (degree , frequency ) in betwenness_map ] , [ frequency for (degree ,frequency ) in betwenness_map ],  'b.')
plt.legend('All Nodes')
plt.xlabel('Overlap')
plt.ylabel('Number of nodes')
plt.title ( "Distribuição do overlap da vizinhança " )

print("Calculando Overlap")

fig2.savefig ( "betwenness_edges.png" )



#
#shortpath_map = sorted(shortpath.items())
#QUESTAO H

#https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.algorithms.centrality.betweenness_centrality.html
#https://networkx.github.io/documentation/networkx-1.9/reference/generated/networkx.algorithms.centrality.edge_betweenness_centrality.html


#QUESTAO I

#https://networkx.github.io/documentation/latest/_modules/networkx/algorithms/bridges.html

#QUESTAO J

#https://networkx.github.io/documentation/networkx-1.9.1/reference/algorithms.assortativity.html
