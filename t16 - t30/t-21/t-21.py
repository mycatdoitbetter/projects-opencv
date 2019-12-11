
import cv2 as cv
import numpy as np

semente = (0, 0)

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
                    if imagem[row + 1, col - 1] < 127:
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


if __name__ == '__main__':
    img_gray = cv.imread('/home/andre/Área de Trabalho/training/codigos/t-21/img-paint.jpg',0)





    cv.namedWindow('img-paint', 1)
    cv.imshow('img-paint', img_gray)
    cv.setMouseCallback('img-paint', marca)
    cv.waitKey(0)


    img_segmentada = crescimento_regioes(img_gray, semente)


    cv.imshow('img-segmentada', img_segmentada)
    cv.waitKey(0)


    cv.imwrite('img-segmentada.jpg', img_segmentada)