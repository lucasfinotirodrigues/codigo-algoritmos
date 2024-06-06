from exibeGrafo import exibir_grafo
import os

def grafo_pre_determinado(): 
        
    grafo = [
        [0, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 0, 1, 0],
        [0, 0, 0, 1, 1, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]

    exibir_grafo(grafo)

    return grafo