def exibir_grafo(grafo):
    print("Grafo:")
    for i, linha in enumerate(grafo):
        conexoes = [str(j) for j, val in enumerate(linha) if val]
        print(f"{i} -> {' '.join(conexoes)}")

def exibir_grafo_com_pesos(grafo):
    print("Grafo com Pesos:")
    for i, linha in enumerate(grafo):
        conexoes = [(j, peso) for j, peso in enumerate(linha) if peso]
        print(f"{i} -> {conexoes}")
