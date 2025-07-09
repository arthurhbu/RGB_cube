'''
    CUBO RGB

O objetivo deste trabalho é implementar a geração de imagens coloridas que sejam "fatias" do cubo que representa o espaço de cor RGB. Você deve numerar os lados deste cubo para referência e escolher uma "fatia" a partir da "fatia inicial" que é uma das faces, a escolher, do cubo.

O programa deve receber como parâmetros:

a face escolhida à partir da qual será selecionada a "fatia" (a face deve ser indexada/rotulada por um valor de 1 a 6)
um valor i (de 0 a 255) para indexar a i-ésima fatia.
O programa deve gerar e mostrar a i-ésima "fatia" em relação à face escolhida como referência.

Considere que no cubo RGB em questão as cores tem profundidade de 24 bits. 

Este trabalho NÃO É a aplicação de uma função pronta. Você deve desenvolver sua própria solução. O método deve ser implementado em Python 3.x, usando-se a biblioteca Numpy. Use a biblioteca OpenCV ou scikit-image para carregar/salvar/mostrar as imagens.

Não há necessidade de utilização de estruturas de repetição explícitas. Priorize a utilização de fatiamento (slicing) no lugar de estruturas de repetição.

'''

import numpy as np

#Face 1: R


bits = 8
cube_dimension = 2**bits

cube = np.zeros((cube_dimension, cube_dimension, cube_dimension, 3), dtype=np.uint8)

def obter_fatia(cube, face, fatia):
    if face == 1:
        return cube[fatia, :, :]
    elif face == 2:
        return cube[:, fatia, :]
    elif face == 3:
        return cube[:, :, fatia]
    elif face == 4:




def main():
    face = int(input('Digite a face do cubo (1 a 6): '))
    if face < 1 or face > 6:
        print('Face inválida')
        return
    
    fatia = int(input('Digite o valor da fatia (0 a 255): '))
    if fatia < 0 or fatia > 255:
        print('Fatia inválida')
        return
    
    fatia = obter_fatia(cube, face, fatia)
    
    print(fatia)
    
if __name__ == '__main__':
    main()
    

    