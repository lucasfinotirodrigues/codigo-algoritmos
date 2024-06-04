from limpaTela import limpaTela
from exibeGrafo import exibir_grafo
import os
from time import sleep

def grafo_hamiltoniano(grafo):

    visitados = set()
    pilha = list(grafo.keys())[0:1]  # Seleciona o primeiro vértice como inicial

    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("-=- Grafos Hamiltonianos -=-")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print(" ")
    print("Esse algoritmo utiliza dos conceitos de Grafos Hamiltonianos")
    print("pra descobrir se é possivel encontrar o camihno Hamiltoniano")
    print("no grafo.")
    print("")
    input("Prescione ENTER para continuar")
    limpaTela()

    exibir_grafo(grafo)
    print(" ")

    visitados = set()
    pilha = list(grafo.keys())[0:1]  # Seleciona o primeiro vértice como inicial

    while pilha:
        atual = pilha.pop()
        if atual not in visitados:
            visitados.add(atual)
            # Adiciona os vizinhos não visitados à pilha
            pilha.extend(vizinho for vizinho in grafo.get(atual, []) if vizinho not in visitados)

    # Verifica se todos os vértices foram visitados
    return len(visitados) == len(grafo)