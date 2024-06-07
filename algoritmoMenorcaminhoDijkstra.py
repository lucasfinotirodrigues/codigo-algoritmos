import heapq
from exibeGrafo import exibir_grafo_com_pesos

def algoritmo_dijkstra(grafo, lista_vertices, src):
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print(" -=- Algoritmo Menor Caminho -=- ")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print(" ")
    print("Utilizaremos o algoritmo de Dijkstra para calcular o menor caminho de um vértice de origem para todos os outros vértices do grafo.")
    print("")
    input("Pressione ENTER para continuar")
    exibir_grafo_com_pesos(grafo)
    print(" ")

    n = len(grafo)
    dist = {vertice: float('inf') for vertice in grafo}
    dist[lista_vertices[src]] = 0
    prev = {vertice: None for vertice in grafo}

    pq = [(0, lista_vertices[src])]
    heapq.heapify(pq)

    while pq:
        current_dist, u = heapq.heappop(pq)
        
        if current_dist > dist[u]:
            continue

        for neighbor, weight in grafo[u]:
            distance = current_dist + weight

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                prev[neighbor] = u
                heapq.heappush(pq, (distance, neighbor))

    print(f"Distâncias a partir do vértice {lista_vertices[src]}:")
    for vertice in dist:
        print(f"Distância até {vertice}: {dist[vertice]}")
    print(" ")

    print("Caminhos:")
    for vertice in prev:
        if prev[vertice] is not None:
            path = []
            step = vertice
            while step is not None:
                path.append(step)
                step = prev[step]
            print(f"Caminho até {vertice}: {' -> '.join(path[::-1])}")
    input("Pressione ENTER para continuar")
