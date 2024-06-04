from limpaTela import limpaTela
from adicionaPeso import adicionar_pesos_aleatorios
from exibeGrafo import exibir_grafo_com_pesos
import os
from time import sleep

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
    limpaTela()

    exibir_grafo_com_pesos(grafo)
    print(" ")
    sleep(1)

    arvore_geradora = set()
    vertices = list(grafo.keys())
    visitados = set()

    vertice_inicial = vertices[0]   
    visitados.add(vertice_inicial)

    while len(visitados) < len(vertices):   # Enquanto houver vértices não visitados
        menor_peso = float('inf')
        aresta_menor_peso = None

        for vertice_visitado in visitados:       # Percorre os vértices visitados
            for vizinho, peso in grafo[vertice_visitado]:   # Percorre os vizinhos e pesos das arestas do vértice visitado
                if vizinho not in visitados and peso < menor_peso:  # Verifica se o vizinho não foi visitado e se o peso é menor que o menor peso registrado
                    menor_peso = peso
                    aresta_menor_peso = (vertice_visitado, vizinho)

        if aresta_menor_peso:    # Se houver uma aresta com menor peso, adiciona na árvore geradora mínima e marca o vértice vizinho como visitado
            arvore_geradora.add(aresta_menor_peso)
            visitados.add(aresta_menor_peso[1])

    return arvore_geradora  # Retorna a árvore geradora mínima encontrada
