def busca_por_profundidade(grafo, lista_vertices):

    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("-=- Algoritmo de Busca por Profundidade -=-")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print(" ")
    print("Esse algoritmo realiza a busca por profundidade no")
    print("grafo a partir do vértice selecionado pelo usuario")
    print("e imprime o resultado.")
    print("")
    input("Prescione ENTER para continuar")


    origem = input("Informe o vértice de origem: ").upper()
    destino = input("Informe o vértice de destino: ").upper()

    if origem not in grafo or destino not in grafo:
        print("Vértice inválido!")
        return

    caminho = []
    visitados = set()

    def dfs(v, destino):
        caminho.append(v)
        visitados.add(v)

        if v == destino:
            return True

        for vizinho in grafo[v]:
            if isinstance(vizinho, tuple):
                vizinho = vizinho[0]
            if vizinho not in visitados:
                if dfs(vizinho, destino):
                    return True

        caminho.pop()
        return False

    if dfs(origem, destino):
        print("Caminho encontrado:", ' -> '.join(caminho))
    else:
        print("Não há caminho entre os vértices.")
