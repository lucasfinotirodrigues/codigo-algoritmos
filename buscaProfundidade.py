from limpaTela import limpaTela
from exibeGrafo import exibir_grafo
import os
from time import sleep

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
    limpaTela()

    exibir_grafo(grafo)
    print(" ")

    while True:
        vertice_inicial = input("Realizar busca por profundidade a partir de qual vértice? ")
        vertice_inicial = vertice_inicial.upper()

        if vertice_inicial not in lista_vertices:
            limpaTela()
            print("O vértice não está no grafo")
            sleep(1)
            limpaTela()
            exibir_grafo(grafo)
            print(" ")
            vertice_inicial = input("Realizar busca por profundidade a partir de qual vértice? ")
            vertice_inicial = vertice_inicial.upper()
        else:
            limpaTela()
            print(" ")
            break
        
    visitados = set() # Lista para armazenar os vértices visitados durante a busca

    def busca(vertice):
        nonlocal visitados
        visitados.add(vertice)     # Adiciona o vértice a lista de visitados
        print(vertice, end=' ')         # E o imprime na tela

        for vizinho in grafo[vertice]:   # Percorre os vizinhos do vértice 
            if vizinho not in visitados:    # Realiza a busca em profundidade para os vizinhos não visitados
                busca(vizinho)

    print("Busca em Profundidade a partir do vértice '{}': ".format(vertice_inicial))
    busca(vertice_inicial)