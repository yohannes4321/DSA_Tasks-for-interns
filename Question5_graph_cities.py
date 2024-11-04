#Parse the file cities.txt to build a graph using the graph class you have modeled

class Graph:
    def __init__(self):
        self.edge={}
        self.used_node=set()
    def add_node(self,node):
        if node not in self.used_node:
            self.used_node.add(node)
            self.edge[node]=[]
        else:
            print(" Node is already present ")
    def add_edge(self,node1,node2,undirected=True):
        if node1 in self.used_node and node2 in self.used_node:
            self.edge[node1].append(node2)
            if undirected is True:
                self.edge[node2].append(node1)
    def print_graph(self):
        for node, edges in self.edge.items():
            print(f"{node} -> {', '.join(edges)}") 
    def build_graph_from_edges(self,edge_list):
       
        
        # Parse the edges and add nodes and edges to the graph
        for line in edge_list:
            source, destination = line.split(',')
            graph.add_node(source.strip())  # Add source city
            graph.add_node(destination.strip())  # Add destination city
            graph.add_edge(source.strip(), destination.strip())  # Add the edge between them

        return graph
# List of edges as provided
edge_list = [
    "New York, Los Angeles",
    "New York, Chicago",
    "New York, Houston",
    "Los Angeles, Chicago",
    "Los Angeles, Houston",
    "Chicago, Houston",
    "San Francisco, Los Angeles",
    "San Francisco, Chicago",
    "San Francisco, Houston",
    "Seattle, Los Angeles",
    "Seattle, Chicago",
    "Seattle, Houston",
    "Boston, Los Angeles",
    "Boston, Chicago",
    "Boston, Houston",
    "Miami, Los Angeles",
    "Miami, Chicago",
    "Miami, Houston"
]

# Build the graph
graph = Graph()
graph = graph.build_graph_from_edges(edge_list)

# Print the graph
graph.print_graph()
