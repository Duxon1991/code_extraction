# networkx best practice getting edge attribute value while iterating over edges
for edge in {(u,v,data) for u,v,data in G.edges_iter(data=True) if data['edge_type']=='foo'}:
    ...