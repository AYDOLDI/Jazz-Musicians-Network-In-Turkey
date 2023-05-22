import networkx as nx
import matplotlib.pyplot as plt

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

filee = open('DistinctPairsCountLastofLast.txt', 'r', encoding="utf-8")
lines2 = filee.readlines()

for i, line in enumerate(lines2):
    line = line.strip()
    linePersons = line.split(',')
    person1 = linePersons[0]
    nextIter = linePersons[1].split('-')
    person2 = nextIter[0]
    weightt = nextIter[1]
    G.add_edge(person1, person2, weight=weightt)

# Grafı çizdirme
pos = nx.circular_layout(G)  # Düğümleri dairesel bir şekilde konumlandırma
nx.draw(G, pos, with_labels=True)

# Kenar ağırlıklarını etiket olarak yazdırma
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

#node_colors = ['red', 'blue', 'green', 'yellow']

# Grafı çizdirme
pos = nx.circular_layout(G)

#nx.draw(G, pos, with_labels=True, node_color=node_colors)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.show()


"""
# Düğümleri ekleme
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')

# Kenarları ve ağırlıkları ekleme
G.add_edge('A', 'B', weight=4)
G.add_edge('B', 'C', weight=2)
G.add_edge('C', 'D', weight=1)
G.add_edge('D', 'A', weight=3)

# Grafı çizdirme
pos = nx.circular_layout(G)  # Düğümleri dairesel bir şekilde konumlandırma
nx.draw(G, pos, with_labels=True)

# Kenar ağırlıklarını etiket olarak yazdırma
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()
"""
