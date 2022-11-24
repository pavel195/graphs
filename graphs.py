# для представления модели графа используем библиотеку networkx
import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
edgess = [('a', 'b', 7), ('a', 'c', 4), ('b', 'f', 7), ('b', 'd', 6), ('c', 'd', 5), ('c', 'e', 5),
          ('d','g',2), ('d','h',7), ('e','g',9), ('h','i',10), ('g','i',4), ('f','h',5)]
G.add_weighted_edges_from(edgess)

pos = nx.planar_layout(G)
p1to6_length = nx.shortest_path_length(G,source='a',target='i',weight='weight')
nx.draw(G,with_labels=1)
plt.savefig("filename.png")
print(p1to6_length)
print(G.nodes)