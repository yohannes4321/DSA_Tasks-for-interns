import csv
from collections import defaultdict, deque
from io import StringIO

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


    # the breadth first search is used to search elements in layer by layer in every step it will cheack all layers 
    # i have used visited  hashset that store alredy used vertex and we will not add them inside the queue and 
    # when elements add to queue when we pop the first element we cheak if it is in visted hash set if it is we will not serach the neighbour just ignore it 
    # and run the while loop run till the queue is empty
    # time complexity O(vertex + edge)
    # space complexiy O(vertex) because we use queue at worst case size of vertex
    def bfs(self, start_vertex, target_vertex):
        visited = set()# create set to store all tarversed vertex nodes
        queue = deque([(start_vertex, [start_vertex])]) # The contain the current node being explored  and the path to reach the node intially start vertex

        while queue:
            # the iteration will run till the queue is empty 
            current_vertex, path = queue.popleft()# pop the first element from the queue 
            if current_vertex == target_vertex:
                print("BFS Path:", " -> ".join(path))
                return path
            if current_vertex not in visited:
                # if the current vertex not in visted hashset it will add it because the hashset helps not to traverse the vertex many times we only traverse it once 

                visited.add(current_vertex)
                for neighbor in self.edge[current_vertex]:
                    # for current vertex cheack all neighbours and if there are not already in visted hash set will append in queue
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))
        print("No path found")
        return None

  
    """the idea how the dfs works is  it goes depth 
    1, there is visted hash set that cheack before the recursive calls  on the vertex it must not be in the visted hash set 
    2 we gona add the current_vertex into visted hash set so it will for next times we willnot add it in call stack
    3 
    2,then we gona call dfs function 
    
    first there is visted hash set it will cheack the """
    def dfs_recursive(self, start_vertex, target_vertex):
        visited = set()
        # intiaize visted set not to visiting them   
        # get the path from dfs and print it
        path = self.dfs(start_vertex, target_vertex, visited, [start_vertex])
        if path:
            print("DFS path:", " -> ".join(path))
        else:
            print("No path found")
        return path
    

    def dfs(self, current_vertex, target_vertex, visited, path):
        if current_vertex == target_vertex:
            # which is the node  vertex currently visted is target index return path
            return path
        visited.add(current_vertex)# add to hash set 
        #
        # to make current vertex visted
        for neighbor in self.edge[current_vertex]:
            # for the vertex it will go to its neigbour all nodes connected to vertex and if they are not in visted set
            #call recurive function 
            if neighbor not in visited:
                # path is list of current path from start to current node new list append to path 
                result_path = self.dfs(neighbor, target_vertex, visited, path + [neighbor])

                if result_path:
                    return result_path
        return None

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

# read csv file using String0
csv_data = StringIO(data)
reader = csv.reader(csv_data)
next(reader)  # Skip header row

 
graph = Graph()
 # intialize and add source and diestination 

for row in reader:
    source, destination = row
    graph.add_vertex(source)
    graph.add_vertex(destination)
    graph.add_edge(source, destination)

 

# Perform BFS and DFS
start_city = "New York"
target_city = "San Francisco"
print("Breadth-First Search:")
graph.bfs(start_city, target_city)

 
print("Depth-First Search ")
graph.dfs_recursive(start_city, target_city)
