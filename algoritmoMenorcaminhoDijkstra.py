import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight  

    def min_distance(self, dist, visited):
        min_dist = sys.maxsize
        min_index = 0

        for v in range(self.V):
            if dist[v] < min_dist and not visited[v]:
                min_dist = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        visited = [False] * self.V

        for _ in range(self.V):
            u = self.min_distance(dist, visited)
            visited[u] = True

            for v in range(self.V):
                if (not visited[v] and self.graph[u][v] and
                        dist[u] + self.graph[u][v] < dist[v]):
                    dist[v] = dist[u] + self.graph[u][v]

        self.print_solution(dist)

    def print_solution(self, dist):
        print("Vertice \tDistancia do vertice de origem")
        for node in range(self.V):
            print(node, "\t\t", dist[node])

# Exemplo de utilização
g = Graph(6)
g.add_edge(0, 1, 7)
g.add_edge(0, 2, 9)
g.add_edge(0, 5, 14)
g.add_edge(1, 2, 10)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 11)
g.add_edge(2, 5, 2)
g.add_edge(3, 4, 6)
g.add_edge(4, 5, 9)

g.dijkstra(0)
