#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 23:18:54 2017

@author: giangblackk
"""

import networkx as nx
from networkx.algorithms import isomorphism
import matplotlib.pyplot as plt
from itertools import combinations

# define (m,n)-tadpole graph = cycle graph m join to path graph n
def tadpole_graph(m,n,create_using=None):
    """Return the Tadpole Graph; `C_m` connected to `P_n`.
    """
    if create_using is not None and create_using.is_directed():
        raise nx.NetworkXError("Directed Graph not supported")
    if m<2:
        raise nx.NetworkXError(\
              "Invalid graph description, m should be >=2")
    if n<0:
        raise nx.NetworkXError(\
              "Invalid graph description, n should be >=0")
    # the cycle
    G=nx.cycle_graph(m,create_using)
    # the stick
    G.add_nodes_from([v for v in range(m,m+n)])
    if n>1:
        G.add_edges_from([(v,v+1) for v in range(m,m+n-1)])
    # connect ball to stick
    if m>0: G.add_edge(m-1,m)
    G.name="cycle_graph(%d,%d)"%(m,n)
    return G

# predefined graph
K23 = nx.complete_bipartite_graph(2,3)
P5 = nx.path_graph(5)
banner = tadpole_graph(3,1)
def able_to_induce_K23_P5_Banner(G):
    GM1 = isomorphism.GraphMatcher(G,K23)
    GM2 = isomorphism.GraphMatcher(G,P5)
    GM3 = isomorphism.GraphMatcher(G,banner)
    if GM1.is_isomorphic() or GM2.is_isomorphic() or GM3.is_isomorphic():
        return True
    return False


def search_dict(dictionary, value):
    for k in dictionary:
        if (dictionary[k] == value):
            return k
    return None

def is_alpha_redundance(G, node):
    # get neigbhors of node in G
    neigbors = G.neighbors(node)
    # for each pair of neigbors v1, v2
    for v1, v2 in combinations(neigbors,2):
        # check if v1, v2 is not neigbors
        if not G.has_edge(v1,v2):
            #check for each u1, u2 in V(G)
            # print(v1,v2)
            neigbors2 = G.neighbors(v1) + list(set(G.neighbors(v2)) - set(G.neighbors(v1)))
            neigbors2 = neigbors + list(set(neigbors2) - set(neigbors)  - set([node]))
            for u1, u2 in combinations(neigbors2,2):
                if not(G.has_edge(u1,node) or G.has_edge(u2,node) or G.has_edge(u1,u2)) and able_to_induce_K23_P5_Banner(G.subgraph([node,u1,u2,v1,v2])):
                     return False
            return True
    return False



def MIN(G):
    H = G.copy()
    I = []
    while H.number_of_nodes() != 0:
        dmin=min(nx.degree(H).values())
        index = search_dict(nx.degree(H), dmin)
        # check alpha-redundance of index  
        # if index is alpha-redundance, remove index from H and next
        # else do like normal
        if is_alpha_redundance(H,index):
            H.remove_node(index)
        else:
            I.append(index)
            H.remove_nodes_from(H.neighbors(index))
            H.remove_node(index)
    IG = G.subgraph(I)
    return IG

## G = nx.read_edgelist(r'/media/giangblackk/6DFEC767661D92C8/MyWorkspace/Graph/projects/MIS/Data/TransportationNetworks_test/Berlin-Friedrichshain/friedrichshain-center_net.edges')
G = nx.Graph(nx.read_pajek(r'/media/giangblackk/6DFEC767661D92C8/MyWorkspace/Graph/projects/MIS/Data/TransportationNetworks_test/Berlin-Friedrichshain/friedrichshain-center_net.net'))
## G = nx.Graph(nx.read_pajek(r'/media/giangblackk/6DFEC767661D92C8/MyWorkspace/Graph/projects/MIS/Data/TransportationNetworks_test/Chicago-regional/ChicagoRegional_net.net'))
## G = nx.Graph(nx.read_pajek(r'/media/giangblackk/6DFEC767661D92C8/MyWorkspace/Graph/projects/MIS/Data/TransportationNetworks_test/Austin/Austin_net.net'))
## G = nx.Graph(nx.read_pajek(r'/media/giangblackk/6DFEC767661D92C8/MyWorkspace/Graph/projects/MIS/Data/TransportationNetworks_test/Anaheim/Anaheim_net.net'))

#G = nx.Graph(nx.read_pajek(r'/media/giangblackk/6DFEC767661D92C8/MyWorkspace/Graph/projects/MIS/Data/TransportationNetworks_test/Berlin-Center/berlin-center_net.net'))
#G = nx.Graph(nx.read_pajek(r'/media/giangblackk/6DFEC767661D92C8/MyWorkspace/Graph/projects/MIS/Data/TransportationNetworks_test/Birmingham-England/Birmingham_Net.net'))
#G = nx.Graph(nx.read_pajek(r'/media/giangblackk/6DFEC767661D92C8/MyWorkspace/Graph/projects/MIS/Data/TransportationNetworks_test/Philadelphia/Philadelphia_net.net'))
#G = nx.Graph(nx.read_pajek(r'/media/giangblackk/6DFEC767661D92C8/MyWorkspace/Graph/projects/MIS/Data/TransportationNetworks_test/Sydney/Sydney_net.net'))
#G = nx.Graph(nx.read_pajek(r'/media/giangblackk/6DFEC767661D92C8/MyWorkspace/Graph/projects/MIS/Data/TransportationNetworks_test/Winnipeg/Winnipeg_net.net'))

IG = MIN(G)
if(IG.number_of_edges() == 0):
    print('Independent set')
else:
    print('Not Independent set')
X = IG.copy()
# print(G.number_of_nodes(),G.number_of_edges())
print(X.number_of_nodes())