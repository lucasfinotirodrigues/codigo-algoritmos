from grafoPreDeterminado import grafo_pre_determinado
from grafoPersonalizado import grafo_personalizado
from exibeGrafo import exibir_grafo, exibir_grafo_com_pesos
from limpaTela import limpaTela
from jsonActions import salvar_grafo, carregar_grafo
from adicionaPeso import adicionar_pesos_aleatorios
from buscaLagura import busca_por_largura
from buscaProfundidade import busca_por_profundidade
from arvoreGeradoraMinima import arvore_geradora_minima
from hamiltoniano import grafo_hamiltoniano
from algoritimosGulosos import busca_gulosa_kruskal
from ordenacaoTopologica import ordenacao_topologica
import os
from time import sleep

listaVertices = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
arquivo = '_database.json'

print(" --=--=--=--=--=--=--=--=--=--=--")
print("|     Python Menu de grafos     |")
print(" --=--=--=--=--=--=--=--=--=--=--")
print()
input("Prescione ENTER para continuar")
limpaTela()

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("|  Algoritmos Avançados          |")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print(" ")
print("Como deseja seu grafo?")
print("=-=-=-=-=-=-=-=-=-=-=-")
print(" 1 - Pré Determinado")
print(" 2 - Faça você mesmo")
print(" 3 - Carregar Grafo Salvo")
tipoGrafo = int(input())

while True:
    if(tipoGrafo < 1 or tipoGrafo > 3):
        print("Numero invalido!")
        sleep(1)
        limpaTela()
        print("Como deseja seu grafo?")
        print("=-=-=-=-=-=-=-=-=-=-=-")
        print(" 1 - Pré Determinado")
        print(" 2 - Faça você mesmo")
        print(" 3 - Carregar Grafo Salvo")
        tipoGrafo = int(input())
    else:
        break

if (tipoGrafo == 1):
    limpaTela()
    grafo = grafo_pre_determinado()

    inicio = 'A'
    final = 'F'
    verticesGrafo = ['A', 'B', 'C', 'D', 'E', 'F']

    print(" ")
elif (tipoGrafo == 2):
    limpaTela()
    grafo, verticesGrafo = grafo_personalizado(listaVertices)

    inicio = verticesGrafo[0]
    final = verticesGrafo[-1]

    limpaTela()
    print(" ")

    while True:
        exibir_grafo(grafo)
        esolha_salvar = input("Deseja salvar seu grafo? [S/N] ")

        if (esolha_salvar.upper() != 'S' and esolha_salvar.upper() != 'N'):
            print("Escolha Invalida!")
            sleep(1)
            limpaTela()
        elif (esolha_salvar.upper() == 'S'):
            possui_pesos = False

            nome_grafo = input("Escolha um nome para seu grafo: ")

            salvar_grafo(nome_grafo, grafo, possui_pesos, arquivo)
            sleep(1)
            print("Grafo salvo com sucesso!")
            sleep(1)
            limpaTela()
            break
        elif (esolha_salvar.upper() == 'N'):
            limpaTela()
            break

elif (tipoGrafo == 3):
    limpaTela()
    possui_pesos = False

    while True:
        print("Carregar Grafo")
        print(" ")
        nome_grafo = input("Nome do grafo a ser carregado: ")

        grafo, verticesGrafo = carregar_grafo(arquivo, nome_grafo)

        if (grafo is not None):
            grafo_selecionado, pesos_selecionados = grafo, possui_pesos
            if pesos_selecionados:
                limpaTela()
                exibir_grafo_com_pesos(grafo_selecionado)
                break
            else:
                limpaTela()
                exibir_grafo(grafo_selecionado)
                break
        else:
            print(f"Grafo com o nome '{nome_grafo}' não encontrado.")
            sleep(1)
            limpaTela()

    print(" ")

print("Selecione seu algoritimo:")
print("=-=-=-=-=-=-=-=-=-=-=-=-=")
print(" ")
print(" 1 - Busca por profundidade")
print(" 2 - Hamiltoniano")
print(" 3 - Busca por Largura")
print(" 4 - Arvore geradora minima")
print(" 5 - Algoritimos gulosos")
print(" 6 - Ordenação topológica")
print(" ")
tipoAlgoritimo = int(input())

while True:
    if(tipoAlgoritimo < 1 or tipoAlgoritimo > 6):
        print("Numero invalido!")
        sleep(1)
        limpaTela()
        print("Selecione seu algoritimo:")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=")
        print(" ")
        print(" 1 - Busca por profundidade")
        print(" 2 - Hamiltoniano")
        print(" 3 - Busca por Largura")
        print(" 4 - Arvore geradora minima")
        print(" 5 - Algoritimos gulosos")
        print(" 6 - Ordenação topológica")
        print(" ")
        tipoAlgoritimo = int(input())
    else:
        limpaTela()
        break

if (tipoAlgoritimo == 1):
    busca_por_profundidade(grafo, verticesGrafo)

elif (tipoAlgoritimo == 2):

    caminho_hamiltoniano = grafo_hamiltoniano(grafo)

    if caminho_hamiltoniano:
        print("Existe um caminho hamiltoniano no grafo.")
    else:
        print("Não existe um caminho hamiltoniano no grafo.")

elif (tipoAlgoritimo == 3):
    caminho_menor = busca_por_largura(grafo, verticesGrafo)
    if caminho_menor:
        exibir_grafo(grafo)
        print(" ")
        print("Caminho mais curto entre:",inicio,"e", final,'=',' -> '.join(caminho_menor))
        print(" ")
    else:
        print("Não há caminho entre os vértices.")

elif (tipoAlgoritimo == 4):
    adicionar_pesos_aleatorios(grafo)

    prim = arvore_geradora_minima(grafo, verticesGrafo)
    print("Árvore Geradora Mínima (Prim):", prim)

elif (tipoAlgoritimo == 5):
    adicionar_pesos_aleatorios(grafo)

    kruskal = busca_gulosa_kruskal(grafo)
    print("Busca Gulosa - Kruskal")
    print(" ")
    print("Árvore Mínima de Abrangência:")
    for aresta in kruskal:
        print(aresta)

elif (tipoAlgoritimo == 6):
    if (tipoGrafo == 1):
        pre_determinado = True
    else:
        pre_determinado = False

    topologica = ordenacao_topologica(grafo, pre_determinado)
    if (topologica) is not None:
        print("Ordenação Topológica:")
        print(topologica)