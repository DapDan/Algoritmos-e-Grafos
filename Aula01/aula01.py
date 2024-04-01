import numpy as np
#import time
#import math
#import random
#import igraph
#import os

"Funcao que pega a instancia, inclui '.txt' e pega a matriz dessa instancia." \
"Imprime a matriz do dataset e o tipo da matriz"
def leitura(inst):
    #diretorio_atual = os.getcwd()
    #print("Diretório atual:", diretorio_atual)

    print("Nome da instancia: ", inst, '\n')
    caminho = 'grafos_datasets/' + inst + '.txt'
    with open(caminho, 'rb') as f:
        data = np.genfromtxt(f, dtype="int64")

    print("Matriz do dataset", inst)
    print(data, '\n')
    print("Tipo da matriz", type(data))
    return data

"Funcao que pega o número de linhas e de colunas do dataset, usando o '.shape'"
def dimensao(inst):
    matriz = leitura(inst)
    matriz_linhas, matriz_colunas = matriz.shape

    #print("\nLinhas: ", matriz_linhas, "\nColunas: ", matriz_colunas)
    return matriz_linhas, matriz_colunas

"""na funcao 'salva' estou armazenando em algumas variaveis os resultados das funcoes 'dimensao' e 'leitura',
para que assim eu possa construir o arquivo onde eu salvo essas informações, assim como pede o exercicio'"""

"""nas linhas 48 a 59, estou criando o arquivo onde vou salvar as informações ditas acima,
assim, o nome do arquivo seria algo como: 'ponte_4x4.txt'
Nas linhas 51 a 53, eu tinha pensado que era pra salvar a matriz toda tambem, como deu um trabalhão
fazer aquele loop, resolvi comentar mesmo.
"""

"""nas linhas 60 a 62, estou salvando no arquivo o Nome, Linhas e Colunas, na linha 66 estou imprimindo
    qual é o nome do arquivo"""

def salva(inst):
    ml, mc = dimensao(inst)
    matriz = leitura(inst)

    caminho_arquivo = inst + '_' + str(ml) + 'x' + str(mc) + '.txt'
    with open(caminho_arquivo, 'w') as arquivo:
        """
        for linha in matriz:
            linha_str = ' '.join(map(str, linha))
            arquivo.write(linha_str + '\n')
        """
        arquivo.write("Nome do arquivo: " + str(caminho_arquivo) + '\n')
        arquivo.write("Linhas: " + str(ml) + '\n')
        arquivo.write("Colunas: " + str(mc))

    print("Valores foram salvos em", caminho_arquivo)

def main():
    instancia = input("Digite o nome da instancia: ")
    #leitura(instancia)
    #dimensao(instancia)
    salva(instancia)


main()