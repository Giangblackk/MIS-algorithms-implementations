#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 14:17:35 2017

@author: giangblackk
"""

import networkx as nx
import matplotlib.pyplot as plt

def search_dict(dictionary, value):
    for k in dictionary:
        if (dictionary[k] == value):
            return k
    return None

def MAX(G):
    H = G.copy()
    I = []
    while H.number_of_edges() != 0:
        dmax=max(nx.degree(H).values())
        index = search_dict(nx.degree(H), dmax)
        H.remove_node(index)
    return H

## G = nx.read_edgelist(r'/media/giangblackk/6DFEC767661D92C8/MyWorkspace/Graph/projects/MIS/Data/TransportationNetworks_test/Berlin-Friedrichshain/friedrichshain-center_net.edges')
## G = nx.Graph(nx.read_pajek(r'/media/giangblackk/6DFEC767661D92C8/MyWorkspace/Graph/projects/MIS/Data/TransportationNetworks_test/Berlin-Friedrichshain/friedrichshain-center_net.net'))
## G = nx.Graph(nx.read_pajek(r'/media/giangblackk/6DFEC767661D92C8/MyWorkspace/Graph/projects/MIS/Data/TransportationNetworks_test/Chicago-regional/ChicagoRegional_net.net'))
## G = nx.Graph(nx.read_pajek(r'/media/giangblackk/6DFEC767661D92C8/MyWorkspace/Graph/projects/MIS/Data/TransportationNetworks_test/Austin/Austin_net.net'))
G = nx.Graph(nx.read_pajek(r'/media/giangblackk/6DFEC767661D92C8/MyWorkspace/Graph/projects/MIS/Data/TransportationNetworks_test/Anaheim/Anaheim_net.net'))

IG = MAX(G)
if(IG.number_of_edges() == 0):
    print('Independent set')
else:
    print('Not Independent set')
X = IG.copy()
