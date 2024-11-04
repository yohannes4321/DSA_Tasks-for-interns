class Graph:
    def __init__(self):
        self.adjacent = {}
        self.used_nodes = set()

    def add_node(self, node):
        if node not in self.used_nodes:
            self.used_nodes.add(node)
            self.adjacent[node] = []
        else:
            print("Node is already present")

    def add_edge(self, node1, node2, undirected=True):
        if node1 in self.used_nodes and node2 in self.used_nodes:
            self.adjacent[node1].append(node2)
            if undirected:
                self.adjacent[node2].append(node1)
        else:
            print("One or both nodes not found in the graph.")

    def print_graph(self):
        for node, edges in self.adjacent.items():
            print(f"{node} -> {', '.join(edges)}")

    def bfs(self, start, goal):
        if start not in self.used_nodes or goal not in self.used_nodes:
            print("Start or goal node not found.")
            return

        queue = [(start, [start])]  # queue of tuples (current_node, path)
        visited = set()

        while queue:
            current, path = queue.pop(0)
            if current == goal:
                print("Path found:", " -> ".join(path))
                return
            if current not in visited:
                visited.add(current)
                for neighbor in self.adjacent[current]:
                    queue.append((neighbor, path + [neighbor]))

        print("No path found from", start, "to", goal)

    def dfs(self, start, goal):
        visited = set()
        path = []

        def dfs_recursive(current):
            if current == goal:
                path.append(current)
                return True
            visited.add(current)
            for neighbor in self.adjacent[current]:
                if neighbor not in visited:
                    if dfs_recursive(neighbor):
                        path.append(current)
                        return True
            return False

        if dfs_recursive(start):
            print("Path found (DFS):", " -> ".join(reversed(path)))
        else:
            print("No path found from", start, "to", goal)

    def dfs_iterative(self, start, goal):
        stack = [(start, [start])]
        visited = set()

        while stack:
            current, path = stack.pop()
            if current == goal:
                print("Path found (DFS Iterative):", " -> ".join(path))
                return
            if current not in visited:
                visited.add(current)
                for neighbor in self.adjacent[current]:
                    stack.append((neighbor, path + [neighbor]))

        print("No path found from", start, "to", goal)
