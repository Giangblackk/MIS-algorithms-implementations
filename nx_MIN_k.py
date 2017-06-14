#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 20:38:48 2017

@author: giangblackk
"""


import networkx as nx
import matplotlib.pyplot as plt

def search_dict(dictionary, value):
    for k in dictionary:
        if (dictionary[k] == value):
            return k
    return None

def max_number_of_neigbour(G):
    max_nneigbours = 0
    for node in G.nodes_iter():
        nneigbour = len(nx.neighbors(G,node))
        if(nneigbour > max_nneigbours):
            max_nneigbours = nneigbour
    return max_nneigbours

def check_condition(G,k):
    for node in G.nodes_iter():
        nneigbour = len(nx.neighbors(G,node))
        if(nneigbour > k):
            return False
    return True
    
def MIN_k(G, k):
    H = G.copy()
    I = []
    while H.number_of_nodes() != 0:
        dmin=min(nx.degree(H).values())
        index = search_dict(nx.degree(H), dmin)
        # print(index)
        tempIG = G.subgraph(I+[index])
        if check_condition(tempIG,k-1):
            I.append(index)
            # print(I)
        H.remove_node(index)
    IG = G.subgraph(I)
    return IG

## G = nx.read_edgelist(r'/media/giangblackk/6DFEC767661D92C8/MyWorkspace/Graph/projects/MIS/Data/TransportationNetworks_test/Berlin-Friedrichshain/friedrichshain-center_net.edges')
## G = nx.Graph(nx.read_pajek(r'/media/giangblackk/6DFEC767661D92C8/MyWorkspace/Graph/projects/MIS/Data/TransportationNetworks_test/Berlin-Friedrichshain/friedrichshain-center_net.net'))
## G = nx.Graph(nx.read_pajek(r'/media/giangblackk/6DFEC767661D92C8/MyWorkspace/Graph/projects/MIS/Data/TransportationNetworks_test/Chicago-regional/ChicagoRegional_net.net'))
## G = nx.Graph(nx.read_pajek(r'/media/giangblackk/6DFEC767661D92C8/MyWorkspace/Graph/projects/MIS/Data/TransportationNetworks_test/Austin/Austin_net.net'))
## G = nx.Graph(nx.read_pajek(r'/media/giangblackk/6DFEC767661D92C8/MyWorkspace/Graph/projects/MIS/Data/TransportationNetworks_test/Anaheim/Anaheim_net.net'))

#G = nx.Graph(nx.read_pajek(r'/media/giangblackk/6DFEC767661D92C8/MyWorkspace/Graph/projects/MIS/Data/TransportationNetworks_test/Berlin-Center/berlin-center_net.net'))
#G = nx.Graph(nx.read_pajek(r'/media/giangblackk/6DFEC767661D92C8/MyWorkspace/Graph/projects/MIS/Data/TransportationNetworks_test/Birmingham-England/Birmingham_Net.net'))
#G = nx.Graph(nx.read_pajek(r'/media/giangblackk/6DFEC767661D92C8/MyWorkspace/Graph/projects/MIS/Data/TransportationNetworks_test/Philadelphia/Philadelphia_net.net'))
#G = nx.Graph(nx.read_pajek(r'/media/giangblackk/6DFEC767661D92C8/MyWorkspace/Graph/projects/MIS/Data/TransportationNetworks_test/Sydney/Sydney_net.net'))
G = nx.Graph(nx.read_pajek(r'/media/giangblackk/6DFEC767661D92C8/MyWorkspace/Graph/projects/MIS/Data/TransportationNetworks_test/Winnipeg/Winnipeg_net.net'))
    
k = 3
IG = MIN_k(G,k)
if(IG.number_of_edges() == 0):
    print('Independent set')
else:
    print('Not Independent set')
X = IG.copy()
print(G.number_of_nodes(),G.number_of_edges())
print(X.number_of_nodes())
