import json

def salvar_grafo(nome_grafo, grafo, peso, nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo_json:
            dados_salvos = json.load(arquivo_json)
    except FileNotFoundError:
        dados_salvos = []

    dados_salvos.append({'nome': nome_grafo, 'grafo': grafo, 'pesos': peso})

    with open(nome_arquivo, 'w') as arquivo_json:
        json.dump(dados_salvos, arquivo_json)

def carregar_grafo(nome_arquivo, nome_grafo):
    try:
        with open(nome_arquivo, 'r') as arquivo_json:
            dados_carregados = json.load(arquivo_json)
    except FileNotFoundError:
        return None, []

    for item in dados_carregados:
        if item['nome'] == nome_grafo:
            grafo = item['grafo']
            verticesGrafo = list(grafo.keys())
            return grafo, verticesGrafo

    return None, []
