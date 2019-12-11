import cv2 as cv
import numpy as np
from numba import njit
semente = (0, 0)

@njit
def crescimento_regioes(imagem, semente=None):
    rows, cols = imagem.shape

    xc, yc = semente

    segmentado = np.zeros_like(imagem)

    segmentado[xc, yc] = 255

    ponto_atual = 0
    ponto_anterior = 1

    while ponto_anterior != ponto_atual:

        ponto_anterior = ponto_atual
        ponto_atual = 0
        for row in range(rows):
            for col in range(cols):

                if segmentado[row, col] == 255:
                    if imagem[row - 1, col - 1] < 127:
                        segmentado[row - 1, col - 1] = 255
                        ponto_atual += 1
                    if imagem[row - 1, col] < 127:
                        segmentado[row - 1, col] = 255
                        ponto_atual += 1
                    if imagem[row - 1, col + 1] < 127:
                        segmentado[row - 1, col + 1] = 255
                        ponto_atual += 1
                    if imagem[row, col - 1] < 127:
                        segmentado[row, col - 1] = 255
                        ponto_atual += 1
                    if imagem[row, col + 1] < 127:
                        segmentado[row, col + 1] = 255
                        ponto_atual += 1
                    if imagem[row + 1, col - 1] < 100:
                        segmentado[row + 1, col - 1] = 255
                        ponto_atual += 1
                    if imagem[row + 1, col] < 127:
                        segmentado[row + 1, col] = 255
                        ponto_atual += 1
                    if imagem[row + 1, col + 1] < 127:
                        segmentado[row + 1, col + 1] = 255
                        ponto_atual += 1

    return segmentado


def marca(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        global semente

        semente = (y, x)

def centroide(imagem):
        # inicializando variaveis para alocar o centroide
        xc, yc = 0, 0
        # capturando tamanho da imagem
        rows,cols = imagem.shape
        #variavel para media
        c = 0
        #buscando semente/pontos do quadrado
        for row in range(rows):
            for col in range(cols):
                if imagem[row,col] == 255:
                    xc += row
                    yc += col
                    c += 1
        xc = int(xc/c)
        yc = int(yc/c)

        return xc, yc

if __name__ == '__main__':
    #abrindo imagem com flag 0 para converter em escala cinza
    img_gray = cv.imread('/home/andre/Área de Trabalho/training/codigos/t-23/kiwi.jpg', 0)

    # criando aba para marcar a semente com clique
    cv.namedWindow('img-paint', 1)
    cv.imshow('img-paint', img_gray)
    cv.setMouseCallback('img-paint', marca)
    cv.waitKey(0)

    #aplicando segmentação
    img_segmentada = crescimento_regioes(img_gray, semente)

    #capturando cordenadas do centroide
    xc, yc = centroide(img_segmentada)

    # criando imagem a ser pintada
    rows,cols = img_segmentada.shape
    img_new = np.zeros([rows, cols, 3], np.uint8)

    #pintando a imagem segmentada de azul, pq a escala do opencv é BGR
    img_new[np.where(img_segmentada == 255)] = [255, 0, 0]

    #desenhando circulo na imagem

    cv.circle(img_new,(yc,xc),3,(0,255,0),-1)

    #mostrando imagem segmentada
    cv.imshow('img-marcada-segmentada', img_new)
    cv.waitKey(0)

    # salvando imagem segmentada
    cv.imwrite('img-segmentada.jpg', img_new)