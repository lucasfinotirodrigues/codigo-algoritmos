from exibeGrafo import exibir_grafo

class AlgoritmoColoracao:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def cor_segura(self, v, cor, cor_atual):
        for i in range(self.V):
            if self.grafo[v][i] == 1 and cor[i] == cor_atual:
                return False
        return True

    def colorir_util(self, num_cores, cor, v):
        if v == self.V:
            return True

        for cor_atual in range(1, num_cores + 1):
            if self.cor_segura(v, cor, cor_atual):
                cor[v] = cor_atual
                if self.colorir_util(num_cores, cor, v + 1):
                    return True
                cor[v] = 0

        return False

    def colorir_grafo(self, num_cores):
        cor = [0] * self.V
        if not self.colorir_util(num_cores, cor, 0):
            print("Não é possível colorir o grafo com", num_cores, "cores.")
            return False

        print("A coloração do grafo é:")
        for v in range(self.V):
            print("Vértice", v, "-> Cor", cor[v])
        return True

def algoritmo_coloracao(grafo, lista_vertices, num_cores):
    vertices_count = len(grafo)
    g = AlgoritmoColoracao(vertices_count)
    for u in grafo:
        for v in grafo[u]:
            g.grafo[lista_vertices.index(u)][lista_vertices.index(v)] = 1
    g.colorir_grafo(num_cores)
