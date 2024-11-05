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

    def add_edge(self, start, end):
        # i have used the Adjecent list techinque for graph which is like linkedlist  for each vertex node we can find the neighbour with traverse throw the linkedlist 
        # if the graph is undirected graph which means no direction is given from the source to destination and destionation to source 
        # for each node we gona append in self.edge[source] the destination 

        self.edge[start].append(end)
        self.edge[end].append(start)

 
    def print_graph(self):
        # for vertex and all the vertex neighbours 
        # self.edge is dictonary key is vertex and value is all neighbors of the vetex in list  print them
        for vertex, neighbors in self.edge.items():
            print(f"{vertex} -> {', '.join(neighbors)}")

    

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

# csv reader the read 
csv_data = StringIO(data)
reader = csv.reader(csv_data)
next(reader)  # Skip header row

 
graph = Graph()

for row in reader:
    source, destination = row
    graph.add_vertex(source)
    graph.add_vertex(destination)
    graph.add_edge(source, destination)

# Display the graph structure
print("Graph:")
graph.print_graph()
 