#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 15:07:37 2017

@author: giangblackk
"""

import networkx as nx
import matplotlib.pyplot as plt

def search_dict(dictionary, value):
    for k in dictionary:
        if (dictionary[k] == value):
            return k
    return None

def node_independent_with_set(G, I, node):
    for vertex in I:
        if G.has_edge(node, vertex):
            return False
    return True

def VO(G):
    degrees = nx.degree(G)
    nodes = degrees.keys()
    nodes = sorted(nodes, key = lambda k: degrees[k])
    I = []
    for node in nodes:
        print(node)
        if node_independent_with_set(G, I, node):
            I.append(node)
    IG = G.subgraph(I)
    return IG

## G = nx.read_edgelist(r'/media/giangblackk/6DFEC767661D92C8/MyWorkspace/Graph/projects/MIS/Data/TransportationNetworks_test/Berlin-Friedrichshain/friedrichshain-center_net.edges')
G = nx.Graph(nx.read_pajek(r'/media/giangblackk/6DFEC767661D92C8/MyWorkspace/Graph/projects/MIS/Data/TransportationNetworks_test/Berlin-Friedrichshain/friedrichshain-center_net.net'))
## G = nx.Graph(nx.read_pajek(r'/media/giangblackk/6DFEC767661D92C8/MyWorkspace/Graph/projects/MIS/Data/TransportationNetworks_test/Chicago-regional/ChicagoRegional_net.net'))
## G = nx.Graph(nx.read_pajek(r'/media/giangblackk/6DFEC767661D92C8/MyWorkspace/Graph/projects/MIS/Data/TransportationNetworks_test/Austin/Austin_net.net'))
## G = nx.Graph(nx.read_pajek(r'/media/giangblackk/6DFEC767661D92C8/MyWorkspace/Graph/projects/MIS/Data/TransportationNetworks_test/Anaheim/Anaheim_net.net'))

IG = VO(G)
if(IG.number_of_edges() == 0):
    print('Independent set')
else:
    print('Not Independent set')
X = IG.copy()
