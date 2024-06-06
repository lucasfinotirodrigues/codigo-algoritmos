from exibeGrafo import exibir_grafo
import os

def grafo_hamiltoniano(): 
        
    grafo = [
        [0, 1, 1, 1, 1, 1, 1, 1]
        [1, 0, 1, 1, 1, 1, 1, 1]
        [1, 1, 0, 1, 1, 1, 1, 1]
        [1, 1, 1, 0, 1, 1, 1, 1]
        [1, 1, 1, 1, 0, 1, 1, 1]
        [1, 1, 1, 1, 1, 0, 1, 1]
        [1, 1, 1, 1, 1, 1, 0, 1]
        [1, 1, 1, 1, 1, 1, 1, 0]
    ]

    exibir_grafo(grafo)

    return grafo
