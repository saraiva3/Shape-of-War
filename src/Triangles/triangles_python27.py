#Author Lucas Saraiva
import re
import networkx as nx
import sys


    

def compute_triangle_and_balance(G):
    triangles = {}    

    ballanced = 0
    unballanced = 0
    print len(G.edges())
    print "Calculating triangles status, it may take a while"
    triadsVisited = set()
    i = 0
    for u in G.nodes():
        viz_u = set(G.neighbors(u))      

        for v in viz_u:
            inter = set(viz_u).intersection(G.neighbors(v))
            for t in inter:

                if (u, v, t) in triadsVisited:
                    continue
                if G.has_edge(t,u): 
                    triadsVisited.add((u,v,t))
                    triadsVisited.add((v,t,u))
                    triadsVisited.add((t,u,v))
                    if G[u][v]["sign"] == -1:
                        edge1 = (v, u)
                    else:
                        edge1 = (u, v)

                    if G[v][t]["sign"]  == -1:
                        edge2 = (t, v)
                    else:
                        edge2 = (v, t)

                    if G[t][u]["sign"]  == -1:
                        edge3 = (u, t)
                    else:
                        edge3 = (t, u)
                    if edge1[1] == edge2[0] and edge2[1] == edge3[0] and edge3[1] == edge1[0]:
                        unballanced = unballanced + 1
                    elif edge3[1] == edge2[0] and edge2[1] == edge1[0] and edge1[1] == edge3[0]:
                        unballanced = unballanced + 1
                    else:
                        ballanced = ballanced + 1  


                elif G.has_edge(u, t):
                    
                    triadsVisited.add((u,v,t))
                    triadsVisited.add((v,t,u))
                    triadsVisited.add((u,t,v))

                    if G[u][v]["sign"] == -1:
                        edge1 = (v, u)
                    else:
                        edge1 = (u, v)

                    if G[v][t]["sign"] == -1:
                        edge2 = (t, v)
                    else:
                        edge2 = (v, t)

                    if G[u][t]["sign"] == -1:
                        edge3 = (t, u)
                    else:
                        edge3 = (u, t)
                    if edge1[1] == edge2[0] and edge2[1] == edge3[0] and edge3[1] == edge1[0]:
                        unballanced = unballanced + 1
                    elif edge3[1] == edge2[0] and edge2[1] == edge1[0] and edge1[1] == edge3[0]:
                        unballanced = unballanced + 1
                    else:
                        ballanced = ballanced + 1  


    print ballanced
    print unballanced

G = nx.DiGraph()

G = nx.read_edgelist('soc-sign-epinions.txt', create_using=nx.DiGraph(), nodetype=int, data=(('sign',int),))
compute_triangle_and_balance(G)


