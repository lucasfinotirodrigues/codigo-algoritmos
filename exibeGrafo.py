def exibir_grafo(grafo):    # Função para exibir os grafos de forma mais apresentavel
    print("Seu Grafo: ")
    for vertice, vizinho in grafo.items():
        print(f"{vertice}: {', '.join(vizinho)}")

def exibir_grafo_com_pesos(grafo):  # Função para exibir os grafos com peso de forma mais apresentavel
    print("Seu Grafo com Pesos:")
    for vertice, vizinhos in grafo.items():
        print(f"{vertice}:", end=' ')
        for vizinho, peso in vizinhos:
            print(f"({vizinho} - {peso})", end=' ')
        print()