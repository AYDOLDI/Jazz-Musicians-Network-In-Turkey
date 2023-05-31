import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter
from networkx.algorithms import community

def Nmaxelements(list1, N):
    final_list = []

    for i in range(0, N):
        max1 = 0

        for j in range(len(list1)):
            if list1[j] > max1:
                max1 = list1[j]

        list1.remove(max1)
        final_list.append(max1)

    print(final_list)
# Boş bir graf oluşturma
#G = nx.Graph()
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
    if (type(person1) or type(person2)) == int:
        break
    edgeWeight = int(nextIter[1])
    G.add_edge(person1, person2, weight=edgeWeight)


#spring layout , pek bi farkı yok
"""
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
degree_threshold = 50
H = G.copy()
d = nx.degree(H)
for n in list(H.nodes()):
    if d[n] <= degree_threshold:
        H.remove_node(n)
nx.draw(H, pos=nx.random_layout(H), with_labels=True, font_size=10)
plt.show()
"""


"""

pos = nx.spring_layout(G2)

# Determine node color and size dynamically
node_color = ["lightblue"] * G2.number_of_nodes()
node_size = [500] * G2.number_of_nodes()

# Modify the node color and size based on some criteria
# For example, let's say node "A" is larger and red


# Draw the nodes, edges, and labels
nx.draw_networkx_nodes(G2, pos, node_color=node_color, node_size=node_size)
nx.draw_networkx_edges(G2, pos, edge_color="black", width=1)
nx.draw_networkx_labels(G2, pos, font_color="green", font_size=12)
nx.draw_networkx_edge_labels(G2, pos, edge_labels=nx.get_edge_attributes(G2, "weight"))

# Display the graph
plt.axis("off")
plt.show()
"""

#histogram ve graph
"""

isolated_nodes = list(nx.isolates(G))  # Bağlantısı olmayan düğümleri bulma

G.remove_nodes_from(isolated_nodes)  # Bağlantısı olmayan düğümleri çıkarma

degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence

# Düğüm boyutunu hesaplamak için normalleştirme yapın
min_size = 100  # Minimum düğüm boyutu
max_size = 1000  # Maksimum düğüm boyutu
sizes = [min_size + (max_size - min_size) * (d - min(degree_sequence)) / (max(degree_sequence) - min(degree_sequence)) for d in degree_sequence]
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())


# Histogramı çizmek için
fig, ax = plt.subplots()
plt.bar(deg, cnt, width=0.80, color='b')
plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")
ax.set_xticks([d + 0.4 for d in deg])
ax.set_xticklabels(deg)

# Grafiği inset olarak çizmek için
plt.axes([0.4, 0.4, 0.5, 0.5])
Gcc = sorted(nx.connected_components(G), key=len, reverse=True)[0]


pos = nx.random_layout(G)
plt.axis('off')
nx.draw_networkx_nodes(G, pos, node_size=sizes)  # Düğüm boyutları sizes listesine göre ayarlanır
nx.draw_networkx_edges(G, pos, alpha=0.4)  # Bağlantıları çizmek için

nx.draw_networkx_labels(G, pos, font_color="black", font_size=5)

plt.savefig("degree_histogram.png")
plt.show()
"""

"""

#nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, "weight"))


isolated_nodes = list(nx.isolates(G))  # Bağlantısı olmayan düğümleri bulma

G.remove_nodes_from(isolated_nodes)  # Bağlantısı olmayan düğümleri çıkarma

degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence

# Düğüm boyutunu hesaplamak için normalleştirme yapın
min_size = 100  # Minimum düğüm boyutu
max_size = 500  # Maksimum düğüm boyutu
sizes = [min_size + (max_size - min_size) * (d - min(degree_sequence)) / (max(degree_sequence) - min(degree_sequence)) for d in degree_sequence]
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())


# Histogramı çizmek için
fig, ax = plt.subplots()
plt.bar(deg, cnt, width=0.80, color='b')
plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")
ax.set_xticks([d + 0.4 for d in deg])
ax.set_xticklabels(deg)

# Grafiği inset olarak çizmek için
plt.axes([0.4, 0.4, 0.5, 0.5])
Gcc = sorted(nx.connected_components(G), key=len, reverse=True)[0]


pos = nx.random_layout(G)
# Draw the nodes, edges, and labels
nx.draw_networkx_nodes(G, pos,  node_size=sizes)
nx.draw_networkx_edges(G, pos, edge_color="#455d7a", width=0.1)
nx.draw_networkx_labels(G, pos, font_color="black", font_size=3)

nx.draw_networkx_labels(G, pos, font_color="black", font_size=5)

plt.show()
"""
"""

isolated_nodes = list(nx.isolates(G))  # Bağlantısı olmayan düğümleri bulma
G.remove_nodes_from(isolated_nodes)  # Bağlantısı olmayan düğümleri çıkarma

#centrality
degree_centrality = nx.degree_centrality(G)
centrality = dict(sorted(degree_centrality.items(), key=itemgetter(1), reverse=True)[:10])
#print("The top N value pairs are " + str(centrality))

#diameter
# Find the connected components
components = list(nx.connected_components(G))

# Compute the diameter for each connected component
for component in components:
    subgraph = G.subgraph(component)
    diameter = nx.diameter(subgraph)
    #print(f"The diameter of the connected component is: {diameter}")


#eigenvector
centrality = nx.eigenvector_centrality(G)
sorted_centrality = sorted(centrality.items(), key=lambda x: x[1], reverse=False)

for node, centrality_value in sorted_centrality:
    centrality_str = "{:.2f}".format(centrality_value)
    #print(f"Vertex: {node}: Eigenvector Centrality {centrality_str}")


#closeness_centrality
closeness = nx.closeness_centrality(G)

#for node, closeness_value in closeness.items():
    #print(f"Node {node}: Closeness Centrality {closeness_value:0.2f}")


#density
density = nx.density(G)

#print(f"The density of the graph is: {density}")



# eccentricity --NOT CONNECTED İSSUE
components = list(nx.connected_components(G))

# Compute the diameter for each connected component
for component in components:
    subgraph = G.subgraph(component)
    eccentricities = nx.eccentricity(subgraph)
    for node, eccentricity in eccentricities.items():
        print(f"The eccentricity of node {node} is: {eccentricity}")
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

"""
"""
# Apply the Girvan-Newman algorithm to find communities
communities = community.girvan_newman(G)

# Get the first level of communities (each subsequent level gives a finer partitioning)
first_communities = next(communities)

# Convert communities generator to list (for drawing)
first_communities = [list(community) for community in first_communities]

# Draw the graph
pos = nx.spring_layout(G)
plt.figure(figsize=(10, 10))

# Draw each community with different colors
for community_index, community in enumerate(first_communities):
    nx.draw_networkx_nodes(G, pos, nodelist=community, node_color=plt.cm.tab10(community_index))

nx.draw_networkx_edges(G, pos)
#plt.show()
"""


num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
connected_components = nx.number_connected_components(G)
degree_centrality = nx.degree_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
num_intermediate_nodes = len(G.edges()) - num_nodes

print("Number of nodes:", num_nodes)
print("Number of edges:", num_edges)
print("Number of connected components:", connected_components)
print("Degree centrality:", degree_centrality)
print("Closeness centrality:", closeness_centrality)
print("Number of intermediate nodes:", num_intermediate_nodes)



















