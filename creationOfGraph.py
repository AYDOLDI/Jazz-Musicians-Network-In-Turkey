import networkx as nx
import matplotlib.pyplot as plt
import scipy as sp
import community as community_louvain

# Boş bir graf oluşturma
G = nx.Graph()

file = open('JazzMusicians text.txt', 'r', encoding="utf-8")
lines = file.readlines()
persons = []
for i, line in enumerate(lines):
    line = line.strip()
    linePersons = line.split(',')
    for j, people in enumerate(linePersons):
        if people not in persons:
            persons.append(people)
file.close()

for k, person in enumerate(persons):
    G.add_node(person)

file2 = open('DistinctPairsCountLastofLast.txt', 'r', encoding="utf-8")
lines2 = file2.readlines()

for i, line in enumerate(lines2):
    line = line.strip()
    linePersons = line.split(',')
    person1 = linePersons[0]
    nextIter = linePersons[1].split('-')
    person2 = nextIter[0]
    edgeWeight = int(nextIter[1])
    G.add_edge(person1, person2, weight=edgeWeight)

#spring layout , pek bi farkı yok
"""" 
pos = nx.spring_layout(G)

# Determine node color and size dynamically
node_color = ["lightblue"] * G.number_of_nodes()
node_size = [500] * G.number_of_nodes()

# Modify the node color and size based on some criteria
# For example, let's say node "A" is larger and red


# Draw the nodes, edges, and labels
nx.draw_networkx_nodes(G, pos, node_color=node_color, node_size=node_size)
nx.draw_networkx_edges(G, pos, edge_color="gray", width=1)
nx.draw_networkx_labels(G, pos, font_color="black", font_size=12)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, "weight"))

# Display the graph
plt.axis("off")
plt.show()
"""

#treshold ile network değil ama diğer graflar çizilebilir. en cok kişiyle çalışanlar gibi.
""" 
# Retain nodes with degree greater than a threshold
degree_threshold = 60
H = G.copy()
d = nx.degree(H)
for n in list(H.nodes()):
    if d[n] <= degree_threshold:
        H.remove_node(n)
nx.draw(H, pos=nx.random_layout(H), with_labels=True, font_size=10)
plt.show()
"""
