import networkx as nx
import matplotlib.pyplot as plt

G = nx.karate_club_graph()

print(G.nodes)
print(G.edges)
nx.draw(G)

G = nx.complete_graph(5)

print(G.nodes)
print(G.edges)
nx.draw(G)

G = nx.petersen_graph()

print(G.nodes)
print(G.edges)

subax1 = plt.subplot(121)
nx.draw(G, with_labels=True, font_weight="bold")
subax2 = plt.subplot(122)
nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight="bold")
