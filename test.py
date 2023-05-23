import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add nodes
nodes = ["A", "B", "C", "D"]
G.add_nodes_from(nodes)

# Add edges with weights
edges = [("A", "B", 3), ("A", "C", 2), ("B", "D", 1), ("A", "D", 4)]
G.add_weighted_edges_from(edges)

# Create a layout for the graph
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
