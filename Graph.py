#Graph from Scratch
from collections import defaultdict, deque

# Graph class
class Graph:
    def __init__(self):
        # Using a defaultdict to automatically create an empty list for new vertices
        self.adj = defaultdict(list)

    # Add an edge to the graph
    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)  # remove this line for directed graph

    # Display the adjacency list
    def display(self):
        for node in self.adj:
            print(f"{node}: {self.adj[node]}")

    # Breadth-First Search
    def bfs(self, start):
        visited = set()
        q = deque([start])
        while q:
            node = q.popleft()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                for neighbor in self.adj[node]:
                    if neighbor not in visited:
                        q.append(neighbor)
        print()

    # Depth-First Search utility
    def dfs_util(self, node, visited):
        print(node, end=" ")
        visited.add(node)
        for neighbor in self.adj[node]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    # Depth-First Search
    def dfs(self, start):
        visited = set()
        self.dfs_util(start, visited)
        print()

    # Detect Cycle (BFS based for undirected graph)
    def has_cycle(self):
        visited = set()
        parent = {}
        q = deque()

        for start in self.adj:
            if start not in visited:
                q.append(start)
                visited.add(start)
                parent[start] = -1

                while q:
                    node = q.popleft()
                    for neighbor in self.adj[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
                            parent[neighbor] = node
                        elif parent[node] != neighbor:
                            return True
        return False

    # Count Connected Components
    def count_components(self):
        visited = set()
        count = 0

        def dfs_component(node):
            visited.add(node)
            for neighbor in self.adj[node]:
                if neighbor not in visited:
                    dfs_component(neighbor)

        for node in self.adj:
            if node not in visited:
                dfs_component(node)
                count += 1
        return count

    # Check if Graph is Bipartite (BFS-based)
    def is_bipartite(self):
        color = {}
        for start in self.adj:
            if start not in color:
                q = deque([start])
                color[start] = 0

                while q:
                    node = q.popleft()
                    for neighbor in self.adj[node]:
                        if neighbor not in color:
                            color[neighbor] = 1 - color[node]
                            q.append(neighbor)
                        elif color[neighbor] == color[node]:
                            return False
        return True

# Example Usage
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)
g.add_edge(5, 6)

print("Graph Adjacency List:")
g.display()

print("\nBFS from 1:")
g.bfs(1)

print("\nDFS from 1:")
g.dfs(1)

print("\nCycle Exists:" if g.has_cycle() else "\nNo Cycle")

print("\nConnected Components:", g.count_components())

print("\nBipartite Graph:" if g.is_bipartite() else "\nNot Bipartite")






#1. Find Number of Connected Components in a Graph

def count_components(graph):
    visited = set()
    count = 0

    def dfs(node):
        visited.add(node)
        for neighbor in graph.adj[node]:
            if neighbor not in visited:
                dfs(neighbor)

    for node in graph.adj:
        if node not in visited:
            dfs(node)
            count += 1
    return count

# Example
print("Connected Components:", count_components(g))






#2. Detect Cycle in an Undirected Graph
def has_cycle(graph):
    visited = set()
    parent = {}
    q = deque()

    for start in graph.adj:
        if start not in visited:
            q.append(start)
            visited.add(start)
            parent[start] = -1

            while q:
                node = q.popleft()
                for neighbor in graph.adj[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
                        parent[neighbor] = node
                    elif parent[node] != neighbor:
                        return True
    return False

# Example
print("Cycle Exists:" if has_cycle(g) else "No Cycle")




#3. Check if Graph is Bipartite
def is_bipartite(graph):
    color = {}
    for start in graph.adj:
        if start not in color:
            q = deque([start])
            color[start] = 0

            while q:
                node = q.popleft()
                for neighbor in graph.adj[node]:
                    if neighbor not in color:
                        color[neighbor] = 1 - color[node]
                        q.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False
    return True

# Example
print("Bipartite Graph:" if is_bipartite(g) else "Not Bipartite")



