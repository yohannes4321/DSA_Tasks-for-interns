import csv
 
from io import StringIO
"""
i have created a graph and to add vertex and add edge remove vertex remove edge finally print the graph and parse the city and print them """
class Graph:
    def __init__(self):
        self.edge ={}

    def add_vertex(self, vertex):
        # to add vertex which means add vertex if it is not alredy exist and 
        # and intialize the vertex with empty array 
        if vertex not in self.edge:
            self.edge[vertex] = []

    def add_edge(self, source, destination):
        # i have used the Adjecent list techinque for graph which is like linkedlist  for each vertex node we can find the neighbour with traverse throw the linkedlist 
        # if the graph is undirected graph which means no direction is given from the source to destination and destionation to source 
        # for each node we gona append in self.edge[source] the destination 

        self.edge[source].append(destination)
        self.edge[destination].append(source)

    def remove_vertex(self, vertex):
        if vertex in self.edge:
            del self.edge[vertex]
            for neighbors in self.edge.values():
                if vertex in neighbors:
                    neighbors.remove(vertex)

    def remove_edge(self, source, destination):
        if source in self.edge and destination in self.edge[source]:
            self.edge[source].remove(destination)
        if destination in self.edge and source in self.edge[destination]:
            self.edge[destination].remove(source)

    def print_graph(self):
        for vertex, neighbors in self.edge.items():
            print(f"{vertex} -> {' '.join(neighbors)}")

    

# Parse the city connection data and build the graph
data = """SourceCity,DestinationCity
New York,Los Angeles
New York,Chicago
New York,Houston
Los Angeles,Chicago
Los Angeles,Houston
Chicago,Houston
San Francisco,Los Angeles
San Francisco,Chicago
San Francisco,Houston
Seattle,Los Angeles
Seattle,Chicago
Seattle,Houston
Boston,Los Angeles
Boston,Chicago
Boston,Houston
Miami,Los Angeles
Miami,Chicago
Miami,Houston"""

# Use csv reader to parse the data from a StringIO object
csv_data = StringIO(data)
reader = csv.reader(csv_data)
next(reader)  # Skip header row

# Create the graph and add vertices and edges
graph = Graph()

for row in reader:
    source, destination = row
    graph.add_vertex(source)
    graph.add_vertex(destination)
    graph.add_edge(source, destination)

# Display the graph structure
print("Graph:")
graph.print_graph()
 