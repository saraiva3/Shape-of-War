# Author Lucas Saraiva Ferreira
import networkx as nx
import matplotlib
import matplotlib . pyplot as plt
from scipy import stats
import numpy as numpy
import powerlaw
matplotlib.use ("agg")



#Insert here your graph file path
print("Reading graph input")
GraphFile = "graphs/graph_version6.gexf"
G = nx.read_gexf(GraphFile)


#Node degree distribution
print("Calculating node degree distribution")
degrees = {}

for node in G.nodes():
	single_degree = G.degree(node)
	if single_degree not in degrees:
		degrees[single_degree] = 0
	degrees[single_degree] += 1

degrees_map = sorted(degrees.items())

#Node degree log log plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.loglog([ degree for (degree , frequency ) in degrees_map ] , [ frequency for (degree ,frequency ) in degrees_map ],  'b.')
plt.legend('Todos nos')
plt.xlabel('Grau')
plt.ylabel('Numero de nos')
plt.title ("Distribuicao do grau dos nos")
plt.xlim([2*10**0, 2*10**2])
fig.savefig ("degree_distribution.png")


#Alpha from linear regression
print("Calculating alpha coefficient")
x = []
y = []
i = 0
for degree, frequency in degrees_map:
	x.append(degree)
	y.append(frequency)

fit_y = powerlaw.Fit(y, discrete=True)
fit_x = powerlaw.Fit(x, discrete=True)
print(fit_y.power_law.alpha)
print(fit_x.power_law.alpha)

#slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)


#Average node degree
print("Calculating average node degree")
sum_of_edges = 0
for node in G.nodes():
	sum_of_edges += G.degree(node)

average_degree = sum_of_edges/len(G)
print(average_degree)


#Components
print("Calculating number of connected components")
print(nx.number_connected_components(G))


#Overlap
print("Calculating node overlap")
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
			

overlap_map = sorted(overlap.items())

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.loglog([ overlap_value for (overlap_value , frequency ) in overlap_map ] , [ frequency for (overlap_value ,frequency ) in overlap_map ],  'b.')
plt.legend("Todos nos")
plt.xlabel('Overlap')
plt.ylabel('Numero de nos')
plt.title ("Distribuição do overlap da vizinhança")
fig2.savefig ( "overlap.png" )


#Path
print("Removing isolates nodes and self loops")
tempgraph = G.copy();
isolate_list = list(nx.isolates(tempgraph))
self_edges = list(nx.nodes_with_selfloops(tempgraph))
#Removing isolates nodes and self loops

for loop in self_edges:
	tempgraph.remove_edge(loop,loop)

for isolated_node in isolate_list:
	tempgraph.remove_node(isolated_node)

print("Calculating average path and all pairs shortest path")
print(nx.average_shortest_path_length(tempgraph))
#Insert print(all_paths) here
all_paths = dict(nx.all_pairs_shortest_path_length(tempgraph, None))

paths = {}
for key,dict2 in all_paths.items():
	for value in dict2.items():		
		if value[1] not in paths:
			paths[value[1]] = 0
		paths[value[1]] += 1

paths_map = sorted(paths.items())

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.plot([ path for (path , frequency ) in paths_map ] , [ frequency for (path ,frequency ) in paths_map ],  'b.')
plt.legend('Todos nos')
plt.xlabel('Tamanho do caminho')
plt.ylabel('Numero de nos')
plt.title ("Distribuição dos caminhos minimos de todos pares")
fig2.savefig ( "all_pair_paths_normal.png" )





print("Calculating Nodes Betwenness")

#Biggest betwenness values to be removed for tests
#G.remove_node("French Empire")
#G.remove_node("Kuwait")
#G.remove_node("Venezuela")
#G.remove_node("Qatar")
#G.remove_node("Haiti")
node_betwenness = nx.betweenness_centrality(G)

betwenness = {}
for key,value in node_betwenness.items():
	if value not in betwenness:
		betwenness[value] = 0
	betwenness[value] += 1

betwenness_map = sorted(betwenness.items())

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.loglog([ degree for (degree , frequency ) in betwenness_map ] , [ frequency for (degree ,frequency ) in betwenness_map ],  'b.')
plt.legend('Todos nos')
plt.xlabel('Betwenness')
plt.ylabel('Numero de nos')
plt.title ("Distribuição do betwennes dos nós")
fig2.savefig ("betwenness_nodes.png")

print("Calculating Edges Betwenness")
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
plt.legend('Todas arestas')
plt.xlabel('Betwenness')
plt.ylabel('Numero de arestas')
plt.title ("Distribuição do betwennes das arestas")
fig2.savefig("betwenness_edges.png")


print("Calculating Assortativity, Assortativity Coef and Pearson Assortativity")

assortativity = nx.degree_assortativity_coefficient(G)
assortatitvity_coef = nx.attribute_assortativity_coefficient(G, "continent")
assortativity_pearson = nx.degree_pearson_correlation_coefficient(G)



print(assortativity)
print(assortatitvity_coef)
print(assortativity_pearson)


print("Calculating Average degree connectivity")
assortativity_list = {}

assort_list = nx.average_degree_connectivity(G)
for key, value in assort_list.items():
	if value not in assortativity_list:
		assortativity_list[value] = 0
	assortativity_list[value] += 1

assortativity_map = sorted(assortativity_list.items())	


fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.loglog([ degree for (degree , frequency ) in assortativity_map ] , [ frequency for (degree ,frequency ) in assortativity_map ],  'b.')
plt.legend('Todos nos')
plt.xlabel('Grau medio da Vizinhanca')
plt.ylabel('Grau')
plt.title ("Distribuição da assortatividade dos nos")
fig2.savefig ("assortativity_nodes.png")