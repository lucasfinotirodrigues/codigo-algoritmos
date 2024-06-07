def arvore_geradora_minima(grafo, lista_vertices):

    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("     -=- Arvores Geradoras Minimas -=-     ")
    print("         -=- Algoritmo de Prim -=-     ")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print(" ")
    print("Esse algoritmo utiliza dos conceitos do algoritmo de Prim em")
    print("Arvores Gerados Minimas de um grafo, para isso será necessario")
    print("adicionar pesos para as aréstas do grafo. Adicionaremos pesos")
    print("aleatórios para cada aresta do seu grafo.")
    print("")
    input("Prescione ENTER para continuar")
    vertices = set(grafo)
    edges = [(weight, u, v) for u in grafo for v, weight in grafo[u]]

    parent = {v: v for v in vertices}
    rank = {v: 0 for v in vertices}

    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(u, v):
        root_u = find(u)
        root_v = find(v)
        if root_u != root_v:
            if rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            else:
                parent[root_u] = root_v
                if rank[root_u] == rank[root_v]:
                    rank[root_v] += 1

    edges.sort()
    mst = set()

    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst.add((u, v, weight))

    return mst
