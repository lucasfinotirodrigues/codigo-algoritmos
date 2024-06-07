from exibeGrafo import exibir_grafo_com_pesos
from limpaTela import limpaTela
from time import sleep

def encontra_componente(componentes, vertice):
    for componente, vertices in componentes.items():
        if vertice in vertices:
            return componente

def busca_gulosa_kruskal(grafo):
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("     -=- Algoritmos Gulosos -=-     ")
    print("    -=- Algoritmo de Kruskal -=-    ")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print(" ")
    print("Esse algoritmo utiliza dos conceitos do algoritmos gulosos em grafos")
    print("utilizando do algoritmo de Kruskal, para realizar uma Árvore Minima de") 
    print("Abrangencia, para isso será necessario adicionar pesos para as aréstas")
    print("do grafo. Adicionaremos pesos Aleatórios para cada aresta do seu grafo.")
    print("")
    input("Pressione ENTER para continuar")
    limpaTela()

    exibir_grafo_com_pesos(grafo)
    print(" ")
    sleep(1)

    arvore = set()
    componentes = {vertice: {vertice} for vertice in grafo}

    arestas = sorted([(u, v, w) for u in grafo for v, w in grafo[u]], key=lambda x: x[2])

    for u, v, w in arestas:
        componente_u = encontra_componente(componentes, u)
        componente_v = encontra_componente(componentes, v)

        if componente_u != componente_v:
            arvore.add((u, v, w))
            componentes[componente_u].update(componentes[componente_v])
            del componentes[componente_v]

            if len(componentes) == 1:
                return arvore

    return arvore
