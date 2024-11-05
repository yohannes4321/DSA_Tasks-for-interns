import csv
from collections import defaultdict, deque
from io import StringIO

class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, source, destination):
        self.adjacency_list[source].append(destination)
        self.adjacency_list[destination].append(source)

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:
            del self.adjacency_list[vertex]
            for neighbors in self.adjacency_list.values():
                if vertex in neighbors:
                    neighbors.remove(vertex)

    def remove_edge(self, source, destination):
        if source in self.adjacency_list and destination in self.adjacency_list[source]:
            self.adjacency_list[source].remove(destination)
        if destination in self.adjacency_list and source in self.adjacency_list[destination]:
            self.adjacency_list[destination].remove(source)

    def print_graph(self):
        for vertex, neighbors in self.adjacency_list.items():
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
 