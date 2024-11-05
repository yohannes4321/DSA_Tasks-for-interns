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

    # the breadth first search is used to search elements in layer by layer in every step it will cheack all layers 
    # i have used visited  hashset that store alredy used vertex and we will not add them inside the queue and 
    # when elements add to queue when we pop the first element we cheak if it is in visted hash set if it is we will not serach the neighbour just ignore it 
    # and run the while loop run till the queue is empty
    # time complexity O(vertex + edge)
    # space complexiy O(vertex) because we use queue at worst case size of vertex
    def bfs(self, start_vertex, target_vertex):
        visited = set()# create set to store all tarversed vertex nodes
        queue = deque([(start_vertex, [start_vertex])]) # use queue 

        while queue:
            # the iteration will run till the queue is empty 
            current_vertex, path = queue.popleft()# pop the first element from the queue and 
            if current_vertex == target_vertex:
                print("BFS Path:", " -> ".join(path))
                return path
            if current_vertex not in visited:
                # if the current vertex not in visted hashset it will add it because the hashset helps not to traverse the vertex many times we only traverse it once 

                visited.add(current_vertex)
                for neighbor in self.adjacency_list[current_vertex]:
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
        path = self._dfs_recursive_helper(start_vertex, target_vertex, visited, [start_vertex])
        if path:
            print("DFS Recursive Path:", " -> ".join(path))
        else:
            print("No path found")
        return path

    def _dfs_recursive_helper(self, current_vertex, target_vertex, visited, path):
        if current_vertex == target_vertex:
            return path
        visited.add(current_vertex)
        for neighbor in self.adjacency_list[current_vertex]:
            if neighbor not in visited:
                result_path = self._dfs_recursive_helper(neighbor, target_vertex, visited, path + [neighbor])
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

 

# Perform BFS and DFS
start_city = "New York"
target_city = "San Francisco"
print("Breadth-First Search:")
graph.bfs(start_city, target_city)

 
print("Depth-First Search ")
graph.dfs_recursive(start_city, target_city)
