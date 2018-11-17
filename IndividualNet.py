# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 23:08:37 2018

@author: panliu
"""

#%%
#print(findperson('Bruce Lee'))
#%%
name = input('input artist name:')
actid = findperson(name)[0]
neighbors = [n for n in G[actid]]
neighbors.append(actid)
G_sub = G.subgraph(neighbors)

plt.figure(figsize=(15,15))
node_size = [10*G_sub.degree(v) for v in G_sub]
pos = nx.spring_layout(G_sub)
edge_width = [2*G_sub[u][v]['weight'] for u,v in G_sub.edges()]
nx.draw_networkx(G_sub, pos=pos, alpha=0.7, node_size=node_size, width=edge_width, node_color='r')
#origin_edges = [x for x in G.edges(data=True) if x[1]==actid or x[0]==actid]
#nx.draw_networkx_edges(G, pos=pos, edgelist=origin_edges, edge_color='g', alpha=0.4, width=2)