#Author Lucas Saraiva

from itertools import chain
import networkx as nx
from networkx.utils import not_implemented_for
import matplotlib
matplotlib.use ("agg")
import matplotlib . pyplot as plt
import bridges as bridges


print("Loading graph file")
GraphFile = "graphs/graph_version6.gexf"
G = nx.read_gexf(GraphFile)

print("Removing self loops and isolated nodes")
isolate_list = list(nx.isolates(G))
self_edges = list(nx.nodes_with_selfloops(G))

for loop in self_edges:
	G.remove_edge(loop,loop)

for isolated_node in isolate_list:
	G.remove_node(isolated_node)
print("Calculating bridges, local brigdes and span")

print(list(bridges.bridges(G)))
print(list(bridges.local_bridges(G,True)))


print("Calculating clustering")
clustering = {}
index = 0
for node in G.nodes():
   clustering[index] = nx.clustering(G,node)   
   index = index + 1 

degrees_map = sorted(clustering.items())
print(nx.average_clustering(G))
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.loglog([ degree for (degree , frequency ) in degrees_map ] , [ frequency for (degree ,frequency ) in degrees_map ],  'b.')
plt.legend('Todos vertices')
plt.xlabel('Grau de clusterizacao')
plt.ylabel('Numero de nos')
plt.title ( "Distribuição do grau de clusterizacao" )
fig2.savefig ( "clustering.png" )