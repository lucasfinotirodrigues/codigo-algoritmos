from exibeGrafo import exibir_grafo
import os

def gerar_grafo_hamiltoniano():  
    grafo = [
        [0, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0]
    ]

    exibir_grafo(grafo)

    return grafo

def verificar_caminho_hamiltoniano(grafo):
    # Implementação simples para verificar um caminho Hamiltoniano.
    # Esta é uma implementação básica e pode precisar de melhorias.
    n = len(grafo)
    visitado = [False] * n
    caminho = []

    def backtrack(atual):
        if len(caminho) == n:
            return True
        for i in range(n):
            if not visitado[i] and grafo[atual][i] == 1:
                visitado[i] = True
                caminho.append(i)
                if backtrack(i):
                    return True
                caminho.pop()
                visitado[i] = False
        return False

    for i in range(n):
        visitado[i] = True
        caminho.append(i)
        if backtrack(i):
            return caminho
        caminho.pop()
        visitado[i] = False

    return None
