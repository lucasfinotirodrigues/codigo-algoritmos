from exibeGrafo import exibir_grafo
import os

def grafo_pre_determinado():    # Função para utilizar um grafo pré determinado
        
    grafo = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    exibir_grafo(grafo)

    return grafo