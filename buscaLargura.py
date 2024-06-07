def busca_por_largura(grafo, lista_vertices):

    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("-=- Algoritmo de Busca por Largura -=-")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print(" ")
    print("Esse algoritmo utiliza dos conceitos de busca por largura")
    print("pra encontrar o caminho mais curto entre dois vértices de")
    print("um grafo.")
    print("")
    input("Prescione ENTER para continuar")

    origem = input("Informe o vértice de origem: ").upper()
    destino = input("Informe o vértice de destino: ").upper()

    if origem not in grafo or destino not in grafo:
        print("Vértice inválido!")
        return None

    queue = [(origem, [origem])]
    visitados = set()

    while queue:
        (vertice, caminho) = queue.pop(0)
        visitados.add(vertice)

        for vizinho in grafo[vertice]:
            if isinstance(vizinho, tuple):
                vizinho = vizinho[0]
            if vizinho not in visitados:
                if vizinho == destino:
                    return caminho + [vizinho]
                else:
                    queue.append((vizinho, caminho + [vizinho]))

    return None
