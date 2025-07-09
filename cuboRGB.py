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
import skimage.io as io
import plotly.graph_objects as go
import matplotlib.animation as animation
import matplotlib.pyplot as plt

#Face 1: R

bits = 8
cube_dimension = 2**bits

axes = np.arange(cube_dimension, dtype=np.uint8)
R, G, B = np.meshgrid(axes, axes, axes, indexing='ij')

rgb_cube = np.stack([R, G , B], axis=-1)


def obter_fatia(cube, face, fatia):
    if face == 1:
        return cube[fatia, :, :, :]
    elif face == 2:
        return cube[fatia, :, :, :]
    elif face == 3:
        return cube[:, fatia, :, :]
    elif face == 4:
        return cube[:, fatia, :, :]
    elif face == 5:
        return cube[:, :, fatia, :]
    elif face == 6:
        return cube[:, :, fatia, :]
    
def plotar_imagem_fatia(fatia):
    io.imshow(fatia)
    io.show()

def plotar_cubo_3d(cube):
    step = 8 # Mostra apenas 1 a cada 16 pontos em cada dimensão
    cube_sample = cube[::step, ::step, ::step, :]
    
    # Extrai as coordenadas e cores do cubo amostrado
    r, g, b = np.indices(cube_sample.shape[:-1])
    cores_rgb_str = [f'rgb({p[0]}, {p[1]}, {p[2]})' for p in cube_sample.reshape(-1, 3)]


    # Cria a figura
    fig = go.Figure(data=[go.Scatter3d(
        x=r.flatten(),
        y=g.flatten(),
        z=b.flatten(),
        mode='markers',
        marker=dict(
            size=4,
            color=cores_rgb_str, # Passa as cores diretamente
            opacity=0.7
        )
    )])

    fig.update_layout(
        title='Cubo RGB 3D Completo (Amostrado)',
        title_x=0.5,
        scene=dict(
            xaxis_title='Red',
            yaxis_title='Green', 
            zaxis_title='Blue',
            xaxis=dict(range=[0, cube_sample.shape[0]]),
            yaxis=dict(range=[0, cube_sample.shape[1]]),
            zaxis=dict(range=[0, cube_sample.shape[2]])
        ),
        margin=dict(l=0, r=0, b=0, t=30)
    )
    fig.show()

def plotar_animacao_fatias(cube, face, im):

    fig, ax = plt.subplots(figsize=(10, 8))
    if face == 1 or face == 2:
        im = ax.imshow(cube[0,:,:,:])
    elif face == 3 or face == 4:
        im = ax.imshow(cube[:,0,:,:])
    elif face == 5 or face == 6:
        im = ax.imshow(cube[:,:,0,:])

    titulo = ax.set_title(f'Fatia 0 - Face {face}', fontsize=14, fontweight='bold')
    ax.axis('off')

    # Adiciona um texto adicional mostrando o progresso
    progresso_texto = ax.text(0.02, 0.98, f'Progresso: 0/{cube_dimension}', 
                             transform=ax.transAxes, fontsize=12, 
                             verticalalignment='top', 
                             bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    def update_frame(i):
        if face == 1 or face == 2:
            nova_fatia = cube[i,:,:,:]
        elif face == 3 or face == 4:
            nova_fatia = cube[:,i,:,:]
        elif face == 5 or face == 6:
            nova_fatia = cube[:,:,i,:]
        
        im.set_data(nova_fatia)
        titulo.set_text(f'Fatia {i} - Face {face}')
        progresso_texto.set_text(f'Progresso: {i}/{cube_dimension}')
        return im, titulo, progresso_texto

    ani = animation.FuncAnimation(fig, update_frame, frames=cube_dimension, 
                                 interval=50, blit=False, repeat=True)
    plt.show()
    

def main():
    face = int(input('Digite a face do cubo (1 a 6): '))
    if face < 1 or face > 6:
        print('Face inválida')
        return
    
    fatia = int(input('Digite o valor da fatia (0 a 255): '))
    if fatia < 0 or fatia > 255:
        print('Fatia inválida')
        return
    
    fatia = obter_fatia(rgb_cube, face, fatia)
    


    # plotar_imagem_fatia(fatia)
    # plotar_cubo_3d(rgb_cube)
    # plotar_cubo_3d_fatia(rgb_cube, fatia)
    plotar_animacao_fatias(rgb_cube, face, fatia)

if __name__ == '__main__':
    main()
    