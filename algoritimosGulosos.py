from limpaTela import limpaTela
from adicionaPeso import adicionar_pesos_aleatorios
from exibeGrafo import exibir_grafo_com_pesos
import os
from time import sleep

def encontra_componente(componentes, vertice):  # Função que busca o componente ao qual um vértice pertence
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
    input("Prescione ENTER para continuar")
    limpaTela()

    exibir_grafo_com_pesos(grafo)
    print(" ")
    sleep(1)

    arvore = set()
    componentes = {vertice: {vertice} for vertice in grafo}

    for u, vizinhos in grafo.items():   # Percorre os vértices do grafo
        for v, w in vizinhos:   # Percorre os vizinhos e pesos das arestas do vértice atual
            componente_u = encontra_componente(componentes, u)
            componente_v = encontra_componente(componentes, v)

            if componente_u != componente_v:     # Se os componentes são diferentes, adiciona a aresta à árvore mínima de abrangência
                arvore.add((u, v, w))   
                componentes[componente_u].update(componentes[componente_v])  # Atualiza os componentes mesclando os conjuntos dos componentes de u e v
                del componentes[componente_v]

                if len(componentes) == 1:   
                    return arvore  # Encerra assim que todos os vértices estiverem conectados

    return arvore    # Retorna a árvore mínima de abrangência encontrada
