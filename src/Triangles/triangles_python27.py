#Author Lucas Saraiva
import re
import networkx as nx
import sys



#Verify ballance based on "Trust in social media" book chapter 5
def verify_balance(G,t):
    if G.get_edge_data(t[0][0],t[0][1]) == -1:
        edge1 = (t[0][1], t[0][0])
    else:
        edge1 = (t[0][0], t[0][1])

    if G.get_edge_data(t[1][0],t[1][1]) == -1:
        edge2 = (t[1][1], t[1][0])
    else:
        edge2 = (t[1][0], t[1][1])
    if G.get_edge_data(t[2][0],t[2][1]) == -1:
        edge3 = (t[2][1], t[2][0])
    else:
        edge3 = (t[2][0], t[2][1])
    if edge1[1] == edge2[0] and edge2[1] == edge3[0] and edge3[1] == edge1[0]:
        return False
    elif edge3[1] == edge2[0] and edge2[1] == edge1[0] and edge1[1] == edge3[0]:
        return False
    else:
        return True

#Verify booth directions to edge and return the right order
def edge_direct(G, node_1, node_2):
    if node_1 in G[node_2]:
        return (node_2, node_1)
    else:
        return (node_1, node_2)

    
#Compute all triangles, based on stack exchange thread
#https://codereview.stackexchange.com/questions/103893/find-a-triangle-in-a-graph-represented-as-an-adjacency-list
def compute_triangle_and_balance(G):
    triangles = {}  

    ballanced = 0
    unballanced = 0
    print len(G.edges())
    #841372
    print "Calculating Triangles and Checking Balance"
    print "This method runs in approximately O(mn), it may take a while"
    for edge in G.edges():      
        for node in G.nodes():
            node1_of_edge = edge[0]
            node2_of_edge = edge[1]
            if G.has_edge(node1_of_edge, node) and G.has_edge(node2_of_edge, node):   
                e1 = edge_direct(G, node1_of_edge, node) 
                e2 = edge_direct(G, node2_of_edge, node)
                t = tuple(sorted((edge,e1 , e2)))
                
                if verify_balance(G, t):
                    ballanced = ballanced + 1                    
                else:
                    unballanced = unballanced + 1

    print "Number of Ballanced Triangles"
    print ballanced
    print "Nunber of Unballanced Triangles"
    print unballanced

    if ballanced > unballanced:
        print "Ballanced network"
    else:
        print "Unballanced network"        

    


print "Reading directed graph file"
G = nx.DiGraph()
G = nx.read_edgelist('soc-sign-epinions.txt', create_using=nx.DiGraph(), nodetype=int, data=(('Sign',int),))
compute_triangle_and_balance(G)


