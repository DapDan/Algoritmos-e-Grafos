'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
SIN110 - ALGORITMOS E GRAFOS
Prof. Rafael Frinhani

Grafos - Programa com funções básicas para práticas de algoritmos em grafos.
Classe principal - desenvolvido em Python 3.10.6

05/09/2022
===================================================='''
import sys

from igraph import *
from Inicializacao import (dataSet as ds, grafo as g, visualizacao as vis)
from Metodos import (caracteristicas as car)

'''Core do programa'''
def main(instancia):
    matriz = ds.criaMatrizAdjacencias(instancia)
    print(matriz, '\n') # '\n' para inserir linha em branco ao final do comando

    G = g.criaGrafo(matriz)
    print(G, '\n') # Mostra as características do grafo.

    vis.visualizarGrafo(False, G)  # True para visualização do grafo ou False.
    funcao1 = car.verificaAdjacencia(matriz, 0, 1)

    resultado = [instancia, funcao1] # Lista de tipo misto com valores dos resultados
    ds.salvaResultado(resultado) # Salva resultado em arquivo

'''Chamada a função main()
   Argumento Entrada: [1] dataset'''
if __name__ == '__main__':
    main(str(sys.argv[1]))

